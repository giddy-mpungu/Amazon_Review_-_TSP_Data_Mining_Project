from mrjob.job import MRJob
from mrjob.step import MRStep
import re

## MultiStep Example
WORD_REGEXP = re.compile(r"[\w']+")


class MRMostFreqWord(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_wordcount,
                    reducer=self.reducer_wordcount),
            MRStep(mapper=self.mapper_freq,
                    reducer=self.reducer_freq),
            MRStep(mapper=self.mapper_most,
                    reducer=self.reducer_most)
        ]

    def mapper_wordcount(self, _, line):
        words = WORD_REGEXP.findall(line)
        for w in words:
            if len(w)>3:
                yield w.lower(), 1
        #for word in line.split():
        #    if len(word)>4:
        #        yield word.lower(), 1 # return only word with at least 3 letters

    def reducer_wordcount(self, word, counts):
        yield word, sum(counts)  # Sum occurrences of each word to get frequency

    def mapper_freq(self, word, total):
        if total > 1:  # Only get words that appear more than once
            yield total, word  # Group them by frequency

    def reducer_freq(self, total, words):
        yield total, words.next()  # .next() gets the first element, so we emit only one word for each frequency

    def mapper_most(self, freq, word):
        yield 'most_used', [freq, word]  # Group all the words together in a list of (frequency, word) tuples

    def reducer_most(self, _, freqs):
        yield 'most_used', max(freqs)  # Get only the most frequent word


if __name__ == '__main__':
    try:
        MRMostFreqWord.run()
    except TypeError:
        print('MrJob cannot work inside iPython Notebook')