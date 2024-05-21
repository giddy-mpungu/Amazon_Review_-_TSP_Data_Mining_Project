from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class AverageHelpfulnessScore(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        helpful_votes = review.get('helpful_vote', 0)
        total_votes = review.get('total_votes', 0)
        yield review['asin'], (helpful_votes, total_votes)

    def reducer_get_average(self, key, values):
        total_helpful = 0
        total_votes = 0
        for helpful, total in values:
            total_helpful += helpful
            total_votes += total
        if total_votes > 0:
            yield None, (total_helpful / total_votes, key)
        else:
            yield None, (0.0, key)

    def reducer_sort(self, _, values):
        sorted_values = sorted(values, reverse=True)
        for avg_helpfulness, product_id in sorted_values:
            yield product_id, avg_helpfulness

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_get_average),
            MRStep(reducer=self.reducer_sort)
        ]

if __name__ == '__main__':
    AverageHelpfulnessScore.run()