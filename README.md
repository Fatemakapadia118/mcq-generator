# MCQ Generator

## 📚 Overview

**MCQ Generator** is an open-source project that enables educators, trainers, and content creators to automatically generate Multiple Choice Questions (MCQs) from various textual sources. Built using Jupyter Notebook, this tool streamlines the process of creating quizzes, assessments, and practice tests—saving hours of manual effort.

## 🚀 Features

- **Automated MCQ Creation**: Input your study material and let the tool draft relevant questions and distractors.
- **Customizable Question Format**: Adjust the number of options, question styles, and difficulty levels.
- **Interactive Notebook Workflow**: Leverage Jupyter's interactivity for real-time editing, preview, and export.
- **Bulk Processing**: Generate large sets of questions from lengthy text or datasets.
- **Export & Integration**: Export MCQs to formats like CSV, PDF, or plain text for integration with e-learning platforms.
- **Extensible Design**: Easily adapt or extend the notebook for specialized domains (science, history, etc).

## 🏗️ Repository Structure

- `mcq-generator.ipynb` : Main Jupyter Notebook with core logic, step-by-step usage, and examples.
- `data/` : (Optional) Sample source material or datasets for demo/testing.
- `requirements.txt` : (If present) Lists Python dependencies for easy setup.
- `README.md` : Project documentation.
- (Other scripts or modules as needed)

## ⚡ Quickstart

### Prerequisites

- **Python 3.8+** (recommended)
- **Jupyter Notebook** (install via Anaconda or pip)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Fatemakapadia118/mcq-generator.git
    cd mcq-generator
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *If `requirements.txt` is not present, manually install packages used in the notebook (e.g., pandas, numpy, nltk, etc).*

### Running the Notebook

1. Start Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Open `mcq-generator.ipynb` in your browser.
3. Follow the notebook cells to:
   - Load or input your source text/data
   - Configure generation parameters
   - Run MCQ generation
   - Review, edit, and export questions

## 🛠️ Example Usage

```python
# Example: Generate MCQs from a text passage
source_text = """
The mitochondria is the powerhouse of the cell. It generates energy through cellular respiration.
"""

questions = generate_mcqs(source_text, num_questions=5)
display(questions)
```

## 🎯 Use Cases

- Teachers preparing quizzes for classroom or online platforms
- Students creating self-practice tests
- HR/training teams generating certification assessments
- Edtech developers automating content generation

## 🤝 Contributing

We welcome contributions! You can:
- Report bugs or request features via GitHub Issues
- Submit pull requests to enhance functionality
- Share feedback and suggestions

## 📄 License

*No license specified yet. Please add an open-source license if you wish others to use/contribute.*

## 👤 Author

- [Fatemakapadia118](https://github.com/Fatemakapadia118)

## 🌐 Links

- **Project Repository:** [github.com/Fatemakapadia118/mcq-generator](https://github.com/Fatemakapadia118/mcq-generator)

---

*For details on configuration, data formats, and advanced usage, see the docstrings and markdown cells inside the main notebook. If you have questions or need help, open an issue in the repository!*
