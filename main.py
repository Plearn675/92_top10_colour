from flask import Flask, render_template, request
from src.color_extractor import extract_top_colors
import os

app = Flask(__name__)

# Where uploaded images are temporarily stored
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    colors = None
    image_url = None

    if request.method == "POST":
        file = request.files["image"]
        delta = int(request.form.get("delta", 20))

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            image_url = filepath

            # Extract raw colors: list of (rgb, count)
            raw_colors = extract_top_colors(filepath, delta=delta)

            total = sum(count for _, count in raw_colors)

            # Convert counts to percentages & hex
            colors = [
                {
                    "rgb": rgb,
                    "hex": "#{:02x}{:02x}{:02x}".format(*rgb),
                    "percent": round((count / total) * 100, 2)
                }
                for rgb, count in raw_colors
            ]

    return render_template("index.html", colors=colors, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
