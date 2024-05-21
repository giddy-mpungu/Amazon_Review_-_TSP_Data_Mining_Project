from mrjob.job import MRJob
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensuring the VADER lexicon is available
nltk.download('vader_lexicon')

class SentimentAnalysis(MRJob):

    def mapper_init(self):
        # Initialize the SentimentIntensityAnalyzer once per mapper instance
        self.sid = SentimentIntensityAnalyzer()

    def mapper(self, _, line):
        review = json.loads(line)
        text = review['text']  # Ensure this matches your data's text field
        sentiment_score = self.sid.polarity_scores(text)
        
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

# python sentiment_analysis.py .\data\all_reviews.jsonl
