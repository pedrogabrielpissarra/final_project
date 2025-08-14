from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detect():
    """
    Endpoint to detect emotion from the input text.
    Returns a formatted string with emotion scores and dominant emotion.
    """    
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # If dominant_emotion is None, return error message
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response text
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result_text

@app.route("/")
def render_index_page():
    """
    This function will render the index page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)