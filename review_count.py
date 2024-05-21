from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class ReviewCountByProduct(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        yield review['asin'], 1

    def reducer_get_count(self, key, values):
        yield None, (sum(values), key)

    def reducer_sort(self, _, values):
        sorted_values = sorted(values, reverse=True)
        for count, product_id in sorted_values:
            yield product_id, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_get_count),
            MRStep(reducer=self.reducer_sort)
        ]

if __name__ == '__main__':
    ReviewCountByProduct.run()
