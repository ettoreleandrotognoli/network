import math
from functools import reduce

def parity_bits_quantity(word_size):
    return int(math.log(word_size,2))+1

def parity_indexes(parity_bit_index, word_size):
    for i in range(parity_bit_index,word_size+1,parity_bit_index*2):
        yield from range(i,min(i+parity_bit_index,word_size+1))

def is_invalid_parity(index,word):
    bits_to_check = parity_indexes(index,len(word))
    bits_values = list(map( lambda bit : word[bit-1], bits_to_check))
    return reduce(lambda a,b : a ^ b,map(bool,map(int,bits_values)))

def check(word):
    size = len(word)
    parities_quantity = parity_bits_quantity(size)
    wrong_bit = 0
    for p in range(parities_quantity):
        index = 2 ** p
        if is_invalid_parity(index,word):
            wrong_bit += index
    if wrong_bit == 0:
        print('ok')
    else:
        print('wrong')

check('1110011')