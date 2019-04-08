#! /usr/bin/env python
import pandas as pd
import glob
import os
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--directory')
    p.add_argument('-o', '--outfile')
    args = p.parse_args()
    outdf = pd.DataFrame(columns = ['Complete', 'Duplicated', 'Fragmented', 'Missing'])
    for n, tab in enumerate(glob.glob(os.path.join(args.directory, "*", "full_table")+"*")):
        name = os.path.basename(tab).replace('full_table_', '').replace('.tsv', '')
        print(name)
        df = pd.read_csv(tab, sep='\t', header=4)
        gp = df.groupby('Status').count().iloc[:,0]
        outdf.loc[name]=gp
    outdf = outdf.fillna(0)
    outdf['Complete_Single']=outdf.Complete -outdf.Duplicated
    outdf['Complete_Duplciated']=outdf.Duplicated
    outdf = outdf.drop('Duplicated', axis=1)
    outdf.to_csv(args.outfile, sep='\t')

if __name__ == '__main__':
    main()
