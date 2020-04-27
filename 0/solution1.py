"""
Solution for (1)
1. solve - serial solution
2. solve_mp - solution using multiprocessing
"""

import multiprocessing as mp
import sys
import random

def generate_numbers(filename):
    """ Generate numbers for the problem """

    random.seed()

    with open(filename, 'w') as f:
        for i in range(1000000):
            f.write("%d\n" % random.randrange(10, 1000000))
        
def check_mp(n):
    """ Check if a string is in the form xx... """

    # This is the version for mp
    first = n[0]
    for i in n[1:]:
        if i != first: return (n,False)
    return (n, True)

def check_s(n):
    """ Check implemented for serial """
    
    first = n[0]
    for i in n[1:]:
        if i != first: return False
    return True

def num_gen(filename):
    """ Number generator for filename """

    for i in open(filename):
        yield i.strip()
        
def solve_mp(filename):
    """ Solve for filename using multiprocessing """

    numbers = []
    p = mp.Pool()

    print('concurrent code')    
    for n,status in p.map(check_mp, num_gen(filename)):
        if status:
            numbers.append(n)
    
    print('matched numbers', numbers)

def solve(filename):
    """ Solve for filename (serial) """

    print('serial code')
    numbers = filter(check_s, num_gen(filename))
    print(list(numbers))
    
if __name__ == "__main__":
    filename = sys.argv[1]
    generate_numbers(filename)
    solve(filename)
    # solve_mp(filename)
