import logging
import azure.functions as func
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    analyzer = SentimentIntensityAnalyzer()
    text = req.params.get("text")
    scores = analyzer.polarity_scores(text)
    sentiment = "positive" if scores["compound"] > 0 else "negative"

    dict_result = {
        'query' : text,
        'sentiment' : sentiment
    }

    func.HttpResponse.mimetype = 'application/json'
    func.HttpResponse.charset = 'utf-8'

    return func.HttpResponse(json.dumps(dict_result))