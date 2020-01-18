# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        # yield key, value
        nw = len(line.split())
        nl = 1
        nc = len(line)
        yield 'words', nw
        yield 'lines', nl
        yield 'chars', nc+1

    def reducer(self, key, values):  # values is a generator
        # yield key, f(values)
        lst = list(values)
        ans = sum(lst)
        yield key, ans

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
