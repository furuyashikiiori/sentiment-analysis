import torch
from transformers import BertTokenizer, BertForSequenceClassification

class SentimentClassifier:
    def __init__(self):
        # BERTのトークナイザとモデルをロード
        self.tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        self.model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        self.model.eval()

    def predict_sentiment(self, text):
        # テキストをトークン化
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        # モデルで推論を行う
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            # 予測ラベルを取得
            predicted_label = torch.argmax(logits, dim=1).item()
            # 感情を判定
            sentiment = self.label_to_sentiment(predicted_label)
        return sentiment

    @staticmethod
    def label_to_sentiment(label):
        if label == 0:
            return "Very Negative"
        elif label == 1:
            return "Negative"
        elif label == 2:
            return "Neutral"
        elif label == 3:
            return "Positive"
        elif label == 4:
            return "Very Positive"
        else:
            return "Unknown"
