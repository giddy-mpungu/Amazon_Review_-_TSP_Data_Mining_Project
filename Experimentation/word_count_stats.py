
from mrjob.job import MRJob

class MRTextInfo(MRJob):
    def mapper(self, _, line):
        for phrase in line.split('.'):
            yield 'phrases', 1
            for word in phrase.split():
                yield 'words', 1
                yield 'characters', len(word)

    def reducer(self, key, counts):
        yield key, sum(counts)


if __name__ == '__main__':
    try:
        MRTextInfo.run()
    except TypeError:
        print('MrJob cannot work inside iPython Notebook as it is not saved as a standalone .py file')