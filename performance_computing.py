# Author: Atheesh Krishnan
# 24th September, 2019

# generic

loops = 25000000
from math import *
a = range(1, loops)
def f(x):
    return 5 * log(x) + cos(x)**2
print('Generic approach:')
%timeit r = [f(x) for x in a]

# numpy

import numpy as np
a = np.arange(1, loops)
print('Numpy approach:')
%timeit r = 5 * np.log(a) + np.cos(a)**2

# numexpr

import numexpr as ne
ne.set_num_threads(1)
f = '5 * log(a) + cos(a)**2'
print('Numexpr Approach: ')
%timeit r = ne.evaluate(f)

# numexpr parallelized with CPU Cores
ne.set_num_threads(4)
print('Numexpr using parallel CPU cores:')
%timeit r = ne.evaluate(f)

