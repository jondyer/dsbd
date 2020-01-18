# Jonathan Dyer
# jbdyer

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        """
        Split each pair of vertices and yield a '1' for each, indicating the
        additional degree that this edge represents for each vertex.
        """
        # yield key, value
        v1, v2 = line.split()
        yield v1, 1
        yield v2, 1


    def reducer_calculate_degrees(self, key, values):  # values is a generator
        """
        This reducer finds the total degree (num of connected vertices) for
        each vertex (key). In order to find the number of vertices with odd
        degree, we'll send all of them to a single reducer with a boolean
        indicating if it has odd degree.
        """
        # yield key, f(values)
        lst = list(values)
        print(key, len(lst))   # print the node and its degree

        if len(lst) % 2 == 1:    # odd degree
            yield None, True
        else:                       # even degree
            yield None, False


    def reducer_check_eulerian(self, key, values):  # values is a generator
        """
        This reducer checks how many vertices have odd degree and outputs
        ("euler", "true") if that number is 0 or 2.
        """
        # yield key, f(values)
        lst = list(values)
        odd = sum(lst)
        if odd==0 or odd==2:
            yield "euler", True
        else:
            yield "euler", False


    def steps(self):
        """
        Defines the steps in this MapReduce job.
        """
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_calculate_degrees),
            MRStep(reducer=self.reducer_check_eulerian)
        ]


if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
