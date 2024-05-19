# Counting the number of reviews for each product
from mrjob.job import MRJob
import json

class ReviewCountByProduct(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        yield review['asin'], 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    ReviewCountByProduct.run()
