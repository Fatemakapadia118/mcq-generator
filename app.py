import streamlit as st
import os, tempfile, json, time

from mcq_generator import (
    extract_text_from_pdf,
    extract_text_from_docx,
    generate_mcqs_from_text,
    export_docx,
)

HISTORY_FILE = "history.json"


# ----------- Helpers for History -----------
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


# ----------- Streamlit UI -----------
st.set_page_config(page_title="MCQ Generator", layout="wide")
st.title("📘 MCQ Generator Dashboard")

# Load history once
if "history" not in st.session_state:
    st.session_state["history"] = load_history()

# Sidebar Controls
st.sidebar.header("⚙️ Settings")
num_questions = st.sidebar.slider("How many MCQs?", 5, 50, 10)
difficulty = st.sidebar.selectbox("Difficulty", ["easy", "medium", "hard"])
mode = st.sidebar.radio("Mode", ["Generate MCQs", "Quiz Mode", "History"])

# File Upload
if mode == "Generate MCQs":
    uploaded_file = st.file_uploader("Upload PDF/DOCX/TXT", type=["pdf", "docx", "txt"])
    if st.button("Generate") and uploaded_file:
        suffix = os.path.splitext(uploaded_file.name)[1].lower()
        tmp_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
        with open(tmp_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        if suffix == ".pdf":
            text = extract_text_from_pdf(tmp_path)
        elif suffix in [".docx", ".doc"]:
            text = extract_text_from_docx(tmp_path)
        else:
            text = uploaded_file.getvalue().decode("utf-8", errors="ignore")

        mcqs = generate_mcqs_from_text(text, num_questions, difficulty)

        if not mcqs:
            st.error("❌ Could not generate MCQs")
        else:
            st.success(f"✅ Generated {len(mcqs)} MCQs")

            for i, q in enumerate(mcqs, 1):
                st.markdown(f"**Q{i}. {q['question']}**")
                for opt in q["options"]:
                    st.markdown(f"- {opt}")
                st.markdown(f"**Answer:** {q['answer']}")
                st.divider()

            # Save DOCX
            out_path = os.path.join(tempfile.gettempdir(), "mcqs.docx")
            export_docx(mcqs, out_path)
            with open(out_path, "rb") as f:
                st.download_button("⬇️ Download as DOCX", f, file_name="mcqs.docx")

            # Save to permanent history
            record = {
                "file": uploaded_file.name,
                "num": num_questions,
                "difficulty": difficulty,
                "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "mcqs": mcqs,
            }
            st.session_state["history"].append(record)
            save_history(st.session_state["history"])


# Quiz Mode
elif mode == "Quiz Mode":
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.quiz_mcqs = []

    if not st.session_state.quiz_mcqs:
        # load latest from history
        if st.session_state["history"]:
            st.session_state.quiz_mcqs = st.session_state["history"][-1]["mcqs"]
        else:
            st.warning("⚠️ No MCQs in history. Generate some first.")

    if st.session_state.quiz_mcqs:
        idx = st.session_state.quiz_index
        mcq = st.session_state.quiz_mcqs[idx]
        st.subheader(f"Q{idx+1}. {mcq['question']}")

        choice = st.radio("Choose an answer:", mcq["options"], key=f"q{idx}")
        if st.button("Submit Answer"):
            if choice == mcq["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong. Correct: {mcq['answer']}")

            st.session_state.quiz_index += 1
            if st.session_state.quiz_index >= len(st.session_state.quiz_mcqs):
                st.balloons()
                st.success(f"🎉 Quiz Finished! Score: {st.session_state.score}/{len(st.session_state.quiz_mcqs)}")
                st.session_state.quiz_index = 0
                st.session_state.score = 0
                st.session_state.quiz_mcqs = []


# History Mode
elif mode == "History":
    st.subheader("📜 Permanent History")
    if not st.session_state["history"]:
        st.info("No history yet.")
    else:
        search = st.text_input("🔍 Search by filename or date")
        for idx, record in enumerate(st.session_state["history"][::-1], 1):
            if search and search.lower() not in record["file"].lower() and search not in record["time"]:
                continue
            with st.expander(f"{idx}. {record['file']} ({record['num']} MCQs, {record['difficulty']}, {record['time']})"):
                for i, q in enumerate(record["mcqs"], 1):
                    st.markdown(f"**Q{i}. {q['question']}**")
                    for opt in q["options"]:
                        st.markdown(f"- {opt}")
                    st.markdown(f"**Answer:** {q['answer']}")
                    st.divider()

                # Redownload
                out_path = os.path.join(tempfile.gettempdir(), f"mcqs_{idx}.docx")
                export_docx(record["mcqs"], out_path)
                with open(out_path, "rb") as f:
                    st.download_button("⬇️ Download Again", f, file_name=f"mcqs_{idx}.docx")
