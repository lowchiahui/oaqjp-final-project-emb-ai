"""
Emotion Detection Flask server that processes the user's input text and returns emotion predictions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the index page with the HTML template.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    Receives the user's input text, processes it to detect emotions, 
    and returns a response with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    emotions = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }

    emotion_str = ", ".join([f"'{emotion}': {score}" for emotion, score in emotions.items()])
    result = (
        f"For the given statement, the system response is {emotion_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
