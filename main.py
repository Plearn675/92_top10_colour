from flask import Flask, render_template, request
from src.color_extractor import extract_top_colors

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            filepath = "samples/" + file.filename
            file.save(filepath)
            colors = extract_top_colors(filepath)
            return render_template("results.html", colors=colors)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
