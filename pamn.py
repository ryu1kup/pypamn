import argparse
import os
import sys
import time

import numpy as np
import pandas as pd
import uproot

from calc import calc

def get_args():
    """
    pypamn user interface
    """

    parser = argparse.ArgumentParser(description="""
        a Python script to analyze multiple nSort output files for nVeto
        """)

    parser.add_argument('-i', '--input', type=str, required=True, nargs='+', help='input filename(s)')
    parser.add_argument('-o', '--output', type=str, default='pypamn_output.csv', help='output filename')
    parser.add_argument('-v', '--verbose', type=int, default=1, help='verbose level')

    args = parser.parse_args()

    ext = args.output.split('.')[-1]
    if ext not in ['csv', 'pkl']:
        raise Exception("Error: Specify the extension from ['csv', 'pkl'] for the output filename")

    return args

def loop(args):
    """
    loop for input files
    """

    dfs = []
    for fin in args.input:
        df_output = pd.DataFrame()
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
        df = uproot.open(fin)['events/events'].arrays(branches=branches, outputtype=pd.DataFrame)
        df_output['NR'] = pd.Series(np.vectorize(calc.element)(df['NR'], 0), index=df.index)
        df_output['Ed'] = pd.Series(np.vectorize(calc.element)(df['Ed'], 0), index=df.index)
        df_output['secondS2'] = pd.Series(np.vectorize(calc.element)(df['S2'], 1), index=df.index)
        df_output['pri'] = pd.Series(np.vectorize(calc.element)(df['typepri'], 0), index=df.index)
        df_output['ns'] = df['ns']
        df_output['fv'] = pd.Series(np.vectorize(calc.fv)(df['X'], df['Y'], df['Y']), index=df.index)
        df_output['nhits'] = pd.Series(np.vectorize(calc.nhits)(df['pmthitid']), index=df.index)
        dfs.append(df_output)
    df_output = pd.concat(dfs)

    ext = args.output.split('.')[-1]
    if ext == 'csv':
        df_output.to_csv(args.output, mode='w', index=None)
    elif ext == 'pkl':
        df_output.to_pickle(args.output)


def main():
    args = get_args()
    loop(args)

if __name__ == '__main__':
    main()
