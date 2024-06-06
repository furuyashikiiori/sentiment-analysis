from flask import Blueprint, request, jsonify, render_template
from app.models.sentiment_model import SentimentClassifier

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']
    
    model = SentimentClassifier()
    sentiment = model.predict_sentiment(text)
    
    return jsonify({'sentiment': sentiment})
