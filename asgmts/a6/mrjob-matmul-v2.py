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
        val = int(val)

        # just to be sure
        if val==0:
            return

        if mat=='A':
            for c in range(c_B):  # the final number of columns, all that matters
                # yield position, value, and which additive term val is in
                yield [row, c], (val, col)

        if mat=='B':
            for r in range(r_A):  # the final num of rows, all that matters
                # yield position, value, and which additive term val is in
                yield [r, col], (val, row)



    def reducer(self, key, values):  # values is a generator
        '''
        Receives all values that belong to this [row,col] (<-- key) in the
        resulting matrix. Looks for values in the same term, multiplies them,
        and adds the result to the total for this position.
        '''
        lst = list(values)
        _, positions = list(zip(*lst))  # extract all term positions we want
        positions = set(positions)   # unique list of all terms

        # now for every position, extract all pairs (or singles) of values
        # then add them to the total for this coordinate
        total = 0
        for i in positions:
            # there should never be more than 2 values assigned to one term
            # this filter returns the entire tuples
            first, *second = list(filter(lambda x: x[1]==i, lst))

            # if there is a second, multiply and add them
            # otherwise one of them is a zero and we can move on
            if second:
                # second will be a list with one tuple, so let's flatten it
                second = second[0]
                total += first[0] * second[0]

        if total:
            yield key, total



if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
