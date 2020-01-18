# Jonathan Dyer
# jbdyer

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        """
        Take each line and separate the jumbled words from dictionary words.
        For jumbled words, prepend a ? and yield with sorted copy as the key.
        For dictionary words, yield with sorted copy as the key.
        """
        # yield key, value
        fields = line.split()
        if fields:
            orig_word = fields[0]
            sort_word = sorted(orig_word)

        if len(fields) > 1:         # this must be a jumbled word
            yield sort_word, '?' + orig_word  # in the form ?_____

        elif len(fields) == 1:      # a dictionary word
            yield sort_word, orig_word


    def reducer(self, key, values):  # values is a generator
        """
        For each alphabetized key, if one of the values is a scrambled word from
        our original list, then yield the scrambled word along with its list of
        solutions.
        """
        # yield key, f(values)
        lst = list(values)
        scrambled = None
        solution = []

        for elem in lst:
            if elem[0]=='?':        # one of our scrambled words!
                scrambled = elem
            else:                   # a possible solution!
                solution.append(elem)

        if scrambled:
            yield len(solution)+1, [scrambled] + solution



if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
