from flask import Blueprint, render_template, request
from models.sentiment_model import SentimentClassifier

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('analyze_sentiment.html')

@bp.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    classifier = SentimentClassifier()
    sentiment = classifier.predict_sentiment(text)
    return render_template('analyze_sentiment.html', text=text, sentiment=sentiment)
