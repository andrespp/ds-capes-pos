# coding: utf-8
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

## Definitions
dataset_home = "./dataset"
datasrc_home = "./datasrc"

datasrc_table = [
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2017-2018-08-01.csv.gz"]]
df = pd.DataFrame(datasrc_table, columns='dataset srcfile'.split())

dataset_table = [
 ["docentes", "br-capes-docentes.parquet"],
 ["discentes", "br-capes-discentes.parquet"],
 ["programas", "br-capes-programas.parquet"]]
ds_df = pd.DataFrame(dataset_table, columns='dataset filename'.split())

## Functions
def read_datasrc(filename, sep=';', encoding='iso-8859-1', index_col=17,
                    columns=False):
    """
       Read csv source file and return a pandas dataframe with its contents. If
       unable to open the file for reading, prints a warning message and return
       -1.

    Optional keyword arguments:
    sep:
    encoding:
    index_col:
    columns: if true return empty dataframe with columns
    """
    try:
        print('Reading {}.'.format(filename))
        # If header==True, return empty dataframe with columns
        if columns:
            return pd.read_csv(filename, index_col=index_col, nrows=0, \
                                sep=sep, encoding=encoding)
        else:
            return pd.read_csv(filename, index_col=index_col, \
                                sep=sep, encoding=encoding)
    except FileNotFoundError:
        print('WARN. Could open "{}".'.format(filename))
        return(-1)

## Main

# 'Programas's dataframe

programas = read_datasrc(datasrc_home + '/' + \
                           df[df['dataset'] == 'programas'].loc[0]['srcfile'],\
                           columns=True)
if not isinstance(programas, pd.DataFrame):
    print('ERROR, can\'t continue')
    exit(-1)

for i in df[df['dataset'] == 'programas']['srcfile']:
    programas = programas.append(read_datasrc(datasrc_home + '/' + i),\
                                    ignore_index=True)

# 'Programa's .parquet file
pq_fname = dataset_home + '/' + \
              ds_df[ds_df['dataset'] == 'programas'].iloc[0]['filename']
pq.write_table(pa.Table.from_pandas(programas), pq_fname, compression='GZIP')
