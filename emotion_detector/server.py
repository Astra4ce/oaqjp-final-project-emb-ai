"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request, render_template
from emotion_detector.emotion_detection import run_emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the homepage of the application.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector():
    """
    Handle emotion detection requests and return formatted response.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = run_emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
