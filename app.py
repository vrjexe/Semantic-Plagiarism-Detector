from flask import Flask, render_template, request, jsonify
from similarity import calculate_similarity

from pypdf import PdfReader
from docx import Document

import os


app = Flask(__name__)

# Maximum uploaded file size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


def extract_text_from_file(file):

    filename = file.filename.lower()

    # ---------------- TXT ----------------

    if filename.endswith(".txt"):

        text = file.read().decode(
            "utf-8",
            errors="ignore"
        )

        return text


    # ---------------- PDF ----------------

    elif filename.endswith(".pdf"):

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text


    # ---------------- DOCX ----------------

    elif filename.endswith(".docx"):

        document = Document(file)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return text


    else:

        raise ValueError(
            "Unsupported file type. Please upload TXT, PDF or DOCX."
        )


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    text1 = data.get("text1", "").strip()
    text2 = data.get("text2", "").strip()


    if not text1 or not text2:

        return jsonify({
            "error": "Please enter text in both boxes."
        }), 400


    try:

        score = calculate_similarity(
            text1,
            text2
        )

        return jsonify({
            "score": round(float(score), 2)
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/upload", methods=["POST"])
def upload():

    try:

        if "file" not in request.files:

            return jsonify({
                "error": "No file uploaded."
            }), 400


        file = request.files["file"]


        if file.filename == "":

            return jsonify({
                "error": "No file selected."
            }), 400


        text = extract_text_from_file(file)


        if not text.strip():

            return jsonify({
                "error": "Could not extract readable text from this file."
            }), 400


        return jsonify({
            "filename": file.filename,
            "text": text
        })


    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400


    except Exception as e:

        return jsonify({
            "error": f"Could not process the file: {str(e)}"
        }), 500


if __name__ == "__main__":

    app.run(debug=True)