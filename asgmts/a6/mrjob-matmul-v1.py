# Jonathan Dyer
# jbdyer

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def configure_args(self):
        super(MR_program, self).configure_args()
        self.add_passthru_arg('-M')

    def mapper(self, _, line):
        '''
        if the value is in matrix A, then use the following:
            row --> send each value to the same row in the output (all columns)
        if in matrix B:
            col --> send each value to the same column in the output (all rows)
        '''
        # get the command-line dimensions as ints
        r_A, c_A, r_B, c_B = list(map(int,self.options.M.split(',')))

        # extract fields from line
        mat, row, col, val = line.split()
        row = int(row)
        col = int(col)

        if mat=='A':
            for c in range(c_B):  # the final number of columns, all that matters
                yield [row, c], val

        if mat=='B':
            for r in range(r_A):  # the final num of rows, all that matters
                yield [r, col], val



    def reducer(self, key, values):  # values is a generator
        '''
        Receives all values that belong to this [row,col] (<-- key) in the
        resulting matrix. Then yields them in sorted order.
        '''
        # yield key, f(values)
        lst = list(values)
        yield key, sorted(lst)



if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
