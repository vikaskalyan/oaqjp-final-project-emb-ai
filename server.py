"""
Server module for Emotion Detection Flask application.

This module exposes a REST endpoint to detect emotions from a given text.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect emotions from user-provided text.

    Query Parameters:
        textToAnalyze (str): Text to analyze.

    Returns:
        str: Formatted response showing emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
