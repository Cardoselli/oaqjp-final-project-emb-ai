"""
Server module for the Emotion Detection application.
This module provides Flask endpoints to analyze text emotions using Watson NLP API.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector, emotion_predictor

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text received from the client and returns the detected emotions.
    Handles invalid or empty input by returning an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    raw_response = emotion_detector(text_to_analyze)
    response = emotion_predictor(raw_response)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    