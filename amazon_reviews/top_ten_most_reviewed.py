 
# Finding the top ten most reviewed products
from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class TopTenMostReviewedProducts(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        yield review['asin'], 1

    def reducer_count_reviews(self, key, values):
        yield None, (sum(values), key)

    def reducer_find_top_ten(self, _, reviews):
        top_ten = sorted(reviews, reverse=True)[:10]
        for count, product_id in top_ten:
            yield product_id, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count_reviews),
            MRStep(reducer=self.reducer_find_top_ten)
        ]

if __name__ == '__main__':
    TopTenMostReviewedProducts.run()
