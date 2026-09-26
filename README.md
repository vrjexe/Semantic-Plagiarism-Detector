# Semantic Plagiarism & Paraphrase Detection

An NLP-based web application that detects **semantic similarity between two pieces of text or documents** using Sentence Transformers and Cosine Similarity.

The system is designed to identify cases where two texts have similar meanings even when different words or sentence structures are used.

> **Important:** A high semantic similarity score indicates that two texts have similar meanings, but the score alone does not prove plagiarism.

---

## 📌 Project Overview

Traditional plagiarism detection systems often rely on exact word or phrase matching.

However, a person can rewrite content using different words while keeping the same meaning. This is known as **paraphrasing**.

This project uses **Natural Language Processing (NLP)** and **sentence embeddings** to compare the semantic meaning of two texts.

### Example

**Original Text:**

> Artificial intelligence is transforming the education sector.

**Submitted Text:**

> AI is changing the way education is delivered.

Although the wording is different, both sentences have a similar meaning.

The system converts both sentences into numerical vectors called **embeddings** and calculates their similarity using **Cosine Similarity**.

---

# 🎯 Objectives

The main objectives of this project are:

* Detect semantic similarity between two texts.
* Identify possible paraphrasing.
* Compare documents based on their meaning rather than only exact words.
* Provide a simple browser-based interface.
* Support manual text input.
* Support TXT, PDF and DOCX document uploads.
* Display the similarity score visually.
* Classify the similarity level.
* Demonstrate the application of NLP and Machine Learning concepts.

---

# 🧠 Technologies Used

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| Python                | Main programming language            |
| Flask                 | Web application backend              |
| HTML                  | Frontend structure                   |
| CSS                   | Frontend styling                     |
| JavaScript            | Frontend interaction                 |
| Sentence Transformers | Text embeddings                      |
| all-MiniLM-L6-v2      | Pre-trained sentence embedding model |
| Scikit-learn          | Cosine similarity calculation        |
| PyPDF                 | PDF text extraction                  |
| python-docx           | DOCX text extraction                 |
| Tkinter               | Earlier prototype GUI                |
| Hugging Face          | Model hosting/cache                  |

---

# 🏗️ System Architecture

```text
                    USER
                     │
                     ▼
             ┌───────────────┐
             │ Web Browser   │
             │ Chrome / Edge │
             └───────┬───────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ HTML + CSS +        │
          │ JavaScript Frontend │
          └──────────┬──────────┘
                     │
                     ▼
              ┌─────────────┐
              │    Flask    │
              │   Backend   │
              └──────┬──────┘
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   Document Extraction      Text Input
   TXT / PDF / DOCX             │
          │                     │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │ Sentence Transformer│
          │ all-MiniLM-L6-v2    │
          └──────────┬──────────┘
                     │
                     ▼
             Text Embeddings
                     │
                     ▼
          ┌─────────────────────┐
          │ Cosine Similarity   │
          └──────────┬──────────┘
                     │
                     ▼
             Similarity Score
                     │
                     ▼
             Browser Result
```

---

# 🔬 How the System Works

The system follows these main steps.

## 1. Input

The user provides two texts.

The user can either:

* Type text manually, or
* Upload a TXT file, or
* Upload a PDF file, or
* Upload a DOCX file.

---

## 2. Text Extraction

For uploaded documents, the Flask backend extracts the readable text.

### TXT

The contents of the text file are directly read.

### PDF

Text is extracted using the `pypdf` library.

### DOCX

Paragraphs are extracted using the `python-docx` library.

---

## 3. Sentence Embedding

The extracted text is passed to the Sentence Transformer model:

```text
all-MiniLM-L6-v2
```

The model converts each text into a numerical vector called a **sentence embedding**.

Conceptually:

```text
Text
  ↓
Sentence Transformer
  ↓
Numerical Embedding
```

---

## 4. Cosine Similarity

The embeddings of the two texts are compared using Cosine Similarity.

The formula is:

```text
                    A · B
Cosine Similarity = ────────
                   ||A|| ||B||
```

Where:

* `A` = embedding of the first text
* `B` = embedding of the second text
* `A · B` = dot product
* `||A||` = magnitude of vector A
* `||B||` = magnitude of vector B

The result is converted into a percentage.

For example:

```text
Similarity = 0.8076

Percentage = 80.76%
```

---

# 📊 Similarity Classification

The application currently uses the following interpretation:

|        Score | Classification                |
| -----------: | ----------------------------- |
|   85% – 100% | Very High Semantic Similarity |
| 70% – 84.99% | High Semantic Similarity      |
| 40% – 69.99% | Moderate Semantic Similarity  |
|    Below 40% | Low Semantic Similarity       |

These thresholds are application-level categories used to present the result clearly. They should not be treated as universal proof of plagiarism.

---

# 🖥️ Features

## Text Comparison

Users can enter two texts directly into the browser.

## Document Upload

The system supports:

```text
.txt
.pdf
.docx
```

## Semantic Analysis

The system compares the meaning of the texts rather than relying only on exact word matching.

## Similarity Score

The result is displayed as a percentage.

Example:

```text
80.76%
```

## Progress Visualization

A visual progress bar represents the similarity score.

## Similarity Classification

The system displays a classification such as:

```text
HIGH SEMANTIC SIMILARITY
```

## Character Counter

The frontend displays the number of characters entered in each text box.

## Responsive UI

The interface is designed to work on different screen sizes.

---

# 📁 Project Structure

```text
Semantic-Plagiarism-Detector/
│
├── app.py
│
├── similarity.py
│
├── test_similarity.py
│
├── README.md
│
├── hf_cache/
│
├── templates/
│   └── index.html
│
└── venv/
```

### File Description

### `app.py`

Contains the Flask web application.

It handles:

* Web routes
* Text comparison requests
* File uploads
* TXT extraction
* PDF extraction
* DOCX extraction
* Communication between frontend and NLP model

---

### `similarity.py`

Contains the main semantic similarity functionality.

It:

1. Loads the Sentence Transformer model.
2. Converts both texts into embeddings.
3. Calculates Cosine Similarity.
4. Converts the result into a percentage.

---

### `test_similarity.py`

Used to test the similarity model independently from the web interface.

Example:

```python
from similarity import calculate_similarity

text1 = "Artificial intelligence is transforming the education sector."

text2 = "AI is changing the way education is delivered."

score = calculate_similarity(text1, text2)

print(f"Semantic Similarity: {score:.2f}%")
```

---

### `templates/index.html`

Contains the complete browser interface including:

* HTML
* CSS
* JavaScript
* Text input
* File upload
* Result visualization

---

# ⚙️ Installation

## 1. Clone or download the project

Open a terminal and navigate to the project directory.

```powershell
cd Semantic-Plagiarism-Detector
```

---

## 2. Create a virtual environment

```powershell
python -m venv venv
```

---

## 3. Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

---

## 4. Install required packages

```powershell
python -m pip install sentence-transformers scikit-learn nltk pandas flask pypdf python-docx
```

---

# ▶️ Running the Application

Run:

```powershell
venv\Scripts\python.exe app.py
```

Flask will start the application.

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

The application should now open in Chrome, Edge, or another modern browser.

---

# 🧪 Testing

A sample test can be performed using the following texts.

### Original

```text
Artificial intelligence is transforming the education sector.
```

### Submitted

```text
AI is changing the way education is delivered.
```

Click:

```text
Analyze Similarity
```

The application will calculate the semantic similarity and display the result.

---

# 📄 Supported Documents

| File Type | Supported |
| --------- | --------- |
| TXT       | ✅         |
| PDF       | ✅         |
| DOCX      | ✅         |
| JPG/PNG   | ❌         |
| XLSX      | ❌         |

The current PDF implementation extracts text from **text-based PDFs**. Scanned/image-only PDFs may require OCR and are not guaranteed to produce readable text.

---

# 🔐 File Size

The Flask application currently limits uploaded files to:

```text
10 MB
```

This prevents unnecessarily large files from being submitted to the application.

---

# 🧩 Main Algorithm

The main algorithm can be summarized as:

```text
START
  │
  ▼
Input Text 1
  │
  ▼
Input Text 2
  │
  ▼
Extract text if files are uploaded
  │
  ▼
Generate embeddings using
all-MiniLM-L6-v2
  │
  ▼
Calculate Cosine Similarity
  │
  ▼
Convert similarity to percentage
  │
  ▼
Classify similarity level
  │
  ▼
Display result
  │
  ▼
END
```

---

# 🤖 Why Sentence Transformers?

Traditional keyword matching can fail when two sentences express the same idea using different words.

For example:

```text
The student completed the assignment.
```

and:

```text
The learner finished the given task.
```

The words are different, but the meanings are similar.

Sentence Transformers generate embeddings that represent the semantic meaning of sentences, allowing the system to compare their meanings.

---

# 📈 Advantages

* Detects semantic similarity.
* Can identify paraphrased content.
* Easy-to-use browser interface.
* Supports multiple document formats.
* Uses a pre-trained NLP model.
* Does not require training a model from scratch.
* Lightweight enough for a local academic project.
* Can be extended with additional features.

---

# ⚠️ Limitations

The current system has several limitations:

1. A similarity score does not prove plagiarism.
2. Very large documents may require additional processing.
3. Scanned PDFs may not contain extractable text.
4. The current system compares two documents at a time.
5. Similarity thresholds are predefined and may need calibration for different datasets.
6. The system does not currently compare documents against a large external corpus or internet database.
7. The system does not currently provide source attribution.

---

# 🚀 Future Enhancements

Possible future improvements include:

* OCR support for scanned PDFs.
* Multiple-document comparison.
* Sentence-level plagiarism detection.
* Highlighting similar sentences.
* Database of previously submitted documents.
* Web-based source comparison.
* Detailed downloadable PDF reports.
* User authentication.
* Similarity history.
* Advanced plagiarism analytics.
* Improved threshold calibration using a validation dataset.
* Visualization of matching/paraphrased sections.

---

# 🎓 Academic Applications

This project can be used as an academic demonstration of:

* Natural Language Processing
* Machine Learning
* Sentence Embeddings
* Vector Representation
* Cosine Similarity
* Flask Web Development
* Document Processing
* Semantic Text Analysis

---

# 👨‍💻 Project Summary

**Project Title:**
Semantic Plagiarism & Paraphrase Detection

**Domain:**
Artificial Intelligence / Natural Language Processing

**Frontend:**
HTML, CSS, JavaScript

**Backend:**
Python Flask

**NLP Model:**
Sentence Transformer — `all-MiniLM-L6-v2`

**Similarity Algorithm:**
Cosine Similarity

**Document Formats:**
TXT, PDF, DOCX

---

# 📜 Disclaimer

This application is intended for educational and academic demonstration purposes.

The semantic similarity score represents the degree of semantic relatedness between two pieces of text. It should not be interpreted as definitive evidence of plagiarism without additional investigation and contextual evidence.

---

# ⭐ Conclusion

The **Semantic Plagiarism & Paraphrase Detection** system demonstrates how NLP techniques can be used to identify semantic relationships between different pieces of text.

By combining a Sentence Transformer model, document text extraction, Cosine Similarity, and a browser-based Flask interface, the project provides a practical demonstration of semantic text comparison.
