import collections

import numpy as np

def element(array, index):
    if len(array) > index:
        return array[index]
    else:
        return np.nan

def fv(X, Y, Z):
    if len(X) > 0:
        r2 = X[0]**2 + Y[0]**2
        z = Z[0] + 739.
        return abs(z / 629.)**3 + (r2 / 396900.)**3
    else:
        return np.nan

def nhits(pmthitid):
    PHE_THRESHOLD = 0.5

    cnts = collections.Counter([i for i in pmthitid if i >= 20000]).values()
    phes = [np.random.normal(loc=c, scale=0.3*c**0.5) if c > 0 else 0 for c in cnts]

    return sum(1 for phe in phes if phe > PHE_THRESHOLD)
