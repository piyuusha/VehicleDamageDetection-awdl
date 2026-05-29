from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/predict"

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None

    if request.method == "POST":

        file = request.files["file"]

        response = requests.post(
            FASTAPI_URL,
            files={"file": (file.filename, file.stream, file.mimetype)}
        )

        result = response.json()

        prediction = result["prediction"]
        confidence = result["confidence"]

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)