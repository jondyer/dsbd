# Template for writing MapReduce programs using mrjob
# % python mrjob-pagerank.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

class MR_program(MRJob):

    def configure_args(self):
        super(MR_program, self).configure_args()
        self.add_passthru_arg('--nodes')    ##  <--- specify which new command line args are used
        self.add_passthru_arg('--beta')    ##  <--- specify which new command line args are used
        self.add_passthru_arg('-N')    ##  <--- specify which new command line args are used

    def mapper_1(self, _, line):
        '''
        Two jobs:
          1) For each out-node from this node, yield (to that node's reducer)
          the pagerank of this node divided by the out-degree of this node. Note
          that the initial pagerank doesn't matter, so we will use 1/num_nodes.
          2) Yield to this node's reducer all the out-nodes it points to.
        '''
        num_nodes = int(self.options.nodes)
        start_pagerank = 1/num_nodes    # initial pagerank
        y, *neighbors = line.split()    # retrieve data

        # job 1)
        for n in neighbors:
            yield n, start_pagerank/len(neighbors)

        # job 2)
        yield y, neighbors


    def reducer_1(self, x, pr_y_by_n_or_nbrs_of_x):
        '''
        This reducer basically has the same two jobs as the mapper above, except
        that here we also calculate the new pagerank with the information given
        in the value list.
        '''
        num_nodes = int(self.options.nodes)
        beta = float(self.options.beta)
        li = list(pr_y_by_n_or_nbrs_of_x)

        # extract the pageranks and neighbors from the value list
        in_pageranks = list(filter(lambda x: not isinstance(x, list), li))
        # this gives us a double list [[...]] so extract the first (only) element
        neighbors = list(filter(lambda x: isinstance(x, list), li))[0]

        # first compute new pagerank
        first_term = (1 - beta) / num_nodes
        second_term = beta * sum(in_pageranks)
        new_pagerank = first_term + second_term

        print(">>>> ", x, new_pagerank)

        # job 1)
        for n in neighbors:
            yield n, new_pagerank/len(neighbors)

        # job 2)
        yield x, neighbors


    def reducer_2(self, x, pr_y_by_n_or_nbrs_of_x):
        '''
        Identical to reducer_1, except here instead of furthering the process
        for some future reducer, we simply calculate the final pagerank and
        yield the output.
        '''
        num_nodes = int(self.options.nodes)
        beta = float(self.options.beta)
        li = list(pr_y_by_n_or_nbrs_of_x)

        # extract the pageranks from the value list
        in_pageranks = list(filter(lambda x: not isinstance(x, list), li))

        # first compute new pagerank
        first_term = (1 - beta) / num_nodes
        second_term = beta * sum(in_pageranks)
        new_pagerank = first_term + second_term

        # yield the solution!
        yield x, new_pagerank


    def steps(self):
        N = int(self.options.N)
        return [MRStep(mapper=self.mapper_1)] + \
               [MRStep(reducer=self.reducer_1)]*N + \
               [MRStep(reducer=self.reducer_2)]


if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
