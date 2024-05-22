from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class AverageRatingByProduct(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        yield review['asin'], review['rating']

    def reducer_get_average(self, key, values):
        ratings = list(values)
        yield None, (sum(ratings) / len(ratings), key)

    def reducer_sort(self, _, values):
        sorted_values = sorted(values, reverse=True)
        for avg_rating, product_id in sorted_values:
            yield product_id, avg_rating

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_get_average),
            MRStep(reducer=self.reducer_sort)
        ]
    
if __name__ == '__main__':
    AverageRatingByProduct.run()

# python average_star_rating.py .\data\Beauty_and_Personal_Care.jsonl >.\results\average_star_rating_byproduct.csv