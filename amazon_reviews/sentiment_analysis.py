from mrjob.job import MRJob
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalysis(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        text = review['text']
        sid = SentimentIntensityAnalyzer()
        sentiment_score = sid.polarity_scores(text)
        
        # Classify sentiment based on compound score
        if sentiment_score['compound'] >= 0.05:
            sentiment = 'positive'
        elif sentiment_score['compound'] <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        yield sentiment, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    SentimentAnalysis.run()
