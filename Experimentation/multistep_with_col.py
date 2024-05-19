from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class GenderCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1,
                   reducer=self.reducer1),
            MRStep(mapper=self.mapper2,
                   reducer=self.reducer2)
        ]

    def mapper1(self, _, line):
        # Use csv.DictReader to parse the line
        if line.startswith('start_station_name'):
            return
        reader = csv.DictReader([line], fieldnames=['start_station_name', 'end_station_name', 'gender'])
        for row in reader:
            yield ((row['gender'], row['start_station_name']), 1)

    def reducer1(self, gender_station, counts):
        yield (gender_station, sum(counts))

    def mapper2(self, gender_station, count):
        gender, station = gender_station
        yield (gender, (station, count))

    def reducer2(self, gender, station_counts):
        # Find the station with the maximum count for this gender
        yield (gender, max(station_counts, key=lambda x: x[1]))

if __name__ == '__main__':
    task1 = GenderCount(args=['citibike.csv'])
    task1.run()