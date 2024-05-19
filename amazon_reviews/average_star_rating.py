# Determine the average star rating for each product

from mrjob.job import MRJob
import json

class AverageRatingByProduct(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        yield review['asin'], review['rating']

    def reducer(self, key, values):
        ratings = list(values)
        yield key, sum(ratings) / len(ratings)

if __name__ == '__main__':
    AverageRatingByProduct.run()
