import collections

import numpy as np

def fv(X, Y, Z):
    return abs((Z[0] + 739.) / 629.)**3 + ((X[0]**2 + Y[0]**2) / 396900.)**3 if len(X) > 0 else np.nan

def nhits(pmthitid):
    PHE_THRESHOLD = 0.5

    cnts = collections.Counter([i for i in pmthitid if i >= 20000]).values()
    phes = [np.random.normal(loc=c, scale=0.3*c**0.5) if c > 0 else 0 for c in cnts]

    return sum(1 for phe in phes if phe > PHE_THRESHOLD)
