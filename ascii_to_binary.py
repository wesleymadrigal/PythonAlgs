#
# Algorithm takes as input any character and returns the binary representation of input character.
#


import math
def ascii_to_bin(char):
        val = ord(char)
        bin_n = '0b'
        length = int(math.floor(math.log(val, 2)))+1
        bin_n += '0'*length
        left_over = val
        bin_list = [i for i in bin_n]
        while left_over > 0:
            if left_over == 1:
                left_over -= 1
                bin_list[len(bin_list)-1] = '1'
            else:
                exponential = int(math.floor(math.log(left_over, 2)))
                bin_list[(len(bin_list)-1)-exponential] = '1'
                left_over -= 2**exponential
        return ''.join(i for i in bin_list)




