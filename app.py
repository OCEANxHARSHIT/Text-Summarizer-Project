from flask import Flask, render_template, request
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Make sure you have templates/index.html

@app.route("/summarize", methods=["POST"])
def summarize():
    input_text = request.form["text"]
    
    if not input_text.strip():
        return "Please enter some text to summarize."

    summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
    return render_template("index.html", summary=summary[0]['summary_text'], original=input_text)

if __name__ == "__main__":
    app.run(debug=True)
