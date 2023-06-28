#!/usr/bin/env python
import numpy as np
import pandas as pd

from math import log, sqrt
from scipy.integrate import quad
from scipy.special import cbrt

from ggplot import *

INPUT_FILE = 'data/primes_1m.txt'
# INPUT_FILE = 'data/primes_1k.txt'

def main(input_file=INPUT_FILE):

    N = 100000

    # read primes from file
    with open(input_file, 'r') as f:
        primes = map(int, list(f))

    primes = primes[: N]        # DEBUG
    max_prime = primes[-1]

    pi_k = 0              # number of primes <= k
    pi_func = list()      # pi_k for various k

    # count primes
    for k in xrange(max_prime):
        try:
            pi_k = 1 + primes.index(k)      # if k is prime, increment pi_k

        except ValueError:
            pass                            # else keep pi_k constant

        pi_func.append(pi_k)

    # calculate approximations
    approx_domain = xrange(2, max_prime)
    approx_1 = [x / log(x) for x in approx_domain]

    Li_x = lambda x: quad(lambda t: 1 / log(t), 2, x)

    # calculate error
    approx = [0, 0] + approx
    err = [1 - x / y for x, y in zip(approx, pi_func) if y > 0]

    # plot differences
    err_df = pd.DataFrame({'x': approx_domain, 'err': err})

    err_plot = (ggplot(err_df, aes('x', 'err'))
        + geom_line()
        + scale_y_continuous(limits=[-0.2, 0.2]))

    print err_plot

    # plot results
    # df = pd.DataFrame({'pi_k': pi_func, 'k': xrange(max_prime)})
    # plot = (ggplot(df, aes('k', 'pi_k')) + geom_line())

    # print (plot + scale_x_continuous(limits=[0, 100])
    #     + scale_y_continuous(limits=[0, 30]))

    # print plot

if __name__ == '__main__':
    main()

# NOTE key fact: primes.index(k) returns a value iff k is prime !
