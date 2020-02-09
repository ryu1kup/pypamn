import argparse
import os
import sys
import collections
import time

import numpy as np
import pandas as pd

import uproot

def get_args():
    """
    pypamn user interface
    """

    parser = argparse.ArgumentParser(description="""
        a Python script to analyze multiple nSort output files for nVeto
        """)

    parser.add_argument('-i', '--input', type=str, required=True, nargs='+', help='input filename(s)')
    parser.add_argument('-o', '--output', type=str, default='pypamn_output.csv', help='output filename')
    parser.add_argument('-c', '--chunksize', type=int, default=10000, help='chunksize')
    parser.add_argument('-v', '--verbose', type=int, default=1, help='verbose level')

    args = parser.parse_args()

    if not args.output.endswith('.csv'):
        raise Exception('Error: Specify the extension .csv for the output filename')

    return args

def loop(args):
    """
    loop for input files
    """

    if os.path.isfile(args.output):
        os.remove(args.output)
    df_output = pd.DataFrame()
    for fin in args.input:
        if args.verbose > 1:
            print('Inputfile:', fin)

        branches = [
                'NR',
                'Ed',
                'S2',
                'typepri',
                'ns',
                'X',
                'Y',
                'Z',
                'pmthitid'
                ]
        for df in uproot.iterate(fin, 'events/events', branches=branches, entrysteps=args.chunksize, outputtype=pd.DataFrame):
            df_output['NR'] = pd.Series(np.vectorize(lambda l: l[0] if len(l) > 0 else np.nan)(df['NR']), index=df.index)
            df_output['Ed'] = pd.Series(np.vectorize(lambda l: l[0] if len(l) > 0 else np.nan)(df['Ed']), index=df.index)
            df_output['secondS2'] = pd.Series(np.vectorize(lambda l: l[1] if len(l) > 1 else np.nan)(df['S2']), index=df.index)
            df_output['pri'] = pd.Series(np.vectorize(lambda l: l[0] if len(l) > 0 else np.nan)(df['typepri']), index=df.index)
            df_output['ns'] = df['ns']
            df_output['fv'] = pd.Series(np.vectorize(calc_fv)(df['X'], df['Y'], df['Y']), index=df.index)
            df_output['nhits'] = pd.Series(np.vectorize(calc_nhits)(df['pmthitid']), index=df.index)
            if not os.path.isfile(args.output):
                df_output.to_csv(args.output, index=None)
            else:
                df_output.to_csv(args.output, mode='a', header=None, index=None)


def calc_nhits(pmthitid):
    PHE_THRESHOLD = 0.5

    cnts = collections.Counter([i for i in pmthitid if i >= 20000]).values()
    phes = [np.random.normal(loc=c, scale=0.3*c**0.5) if c > 0 else 0 for c in cnts]

    return sum(1 for phe in phes if phe > PHE_THRESHOLD)

def calc_fv(X, Y, Z):
    if len(X) > 0:
        return abs((Z[0] + 739.) / 629.)**3 + ((X[0]**2 + Y[0]**2) / 396900.)**3
    else:
        return np.nan

def main():
    args = get_args()
    loop(args)

if __name__ == '__main__':
    main()
