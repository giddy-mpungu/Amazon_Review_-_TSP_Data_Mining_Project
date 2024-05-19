# Calculating the average helpfulness score for reviews

from mrjob.job import MRJob
import json

class AverageHelpfulnessScore(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        helpful_votes = review['helpful_votes']
        total_votes = review['helpful_votes'] + review['total_votes']
        yield review['asin'], (helpful_votes, total_votes)

    def reducer(self, key, values):
        total_helpful = 0
        total_votes = 0
        for helpful, total in values:
            total_helpful += helpful
            total_votes += total
        yield key, total_helpful / total_votes

if __name__ == '__main__':
    AverageHelpfulnessScore.run()
