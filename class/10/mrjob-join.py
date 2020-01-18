# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        # yield key, value
        fields = line.split('|')
        if len(fields) == 2:
            country, code = fields
        else:
            customer, comment, code = fields

        yield code, fields

    def reducer(self, key, values):  # values is a generator
        # yield key, f(values)
        lst = list(values)
        T1 = []
        T2 = []

        for x in lst:
            if len(x)==2:
                T1.append(x)
            else:
                T2.append(x)

        for y in T2:
            if T1:
                yield key, T1[0] + y

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
