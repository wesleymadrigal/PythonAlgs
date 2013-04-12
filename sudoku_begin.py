# the below code will generate a 9x9 sudoku puzzle and the output will have exactly 1-9 in each row and the
# very last column will also be properly solved as sudoku should be, the other columns
# are still needing work

import random

def make_sudoku():
        l = [[0 for i in range(9)] for i in range(9)]
        count = 0
        for row in l:
                for e in range(len(l)):
                        row[e] = random.randint(1,9)
                        while row.count(row[e]) != 1:
                                row[e] = random.randint(1,9)
                                count += 1
        for each in range(len(l)):
                cur = [row[each] for row in l]
                for i in range(len(cur)):
                        n = random.randint(1,9)
                        old_cur = cur[i]
                        row_n_loc = l[i].index(n)
                        cur[i] = n
                        l[i][each] = n
                        l[i][row_n_loc] = old_cur
                        while cur.count(cur[i]) != 1:
                                n = random.randint(1,9)
                                cur_original = cur[i]
                                cur[i] = n
                                origin_row_n_index = l[i].index(n)
                                l[i][each] = n
                                l[i][origin_row_n_index] = cur_original
                                count += 1
        return l, count


def main():
        the_sudoku, the_count = make_sudoku()
        for i in the_sudoku:
                print i
        print the_count


if __name__ == '__main__':
        main()
