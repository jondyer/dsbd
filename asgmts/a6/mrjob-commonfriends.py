# Jonathan Dyer
# jbdyer

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        '''
        Take each line of friends and split into pairs. For each unique pair,
        yield all the friends in this list (i.e. all friends of the person we're
        currently considering).
        '''
        # first extract fields
        person, friends = line.split(':')
        person = person.strip()
        friends = friends.split()

        for f in friends:
            yield sorted((person, f)), friends


    def reducer(self, key, values):  # values is a generator
        '''
        For each unique pair of friends, there will be a list of two lists,
        containing all the friends of the first and second person, resp. This
        reducer takes this input and yields the intersection of these two sets.
        '''
        # yield key, f(values)
        lst = list(values)
        f1, f2 = lst        # split into two friend groups
        s1 = set(f1)        # convert to sets
        s2 = set(f2)

        yield key, sorted(s1.intersection(s2))


if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
