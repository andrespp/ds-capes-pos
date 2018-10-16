# coding: utf-8
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

## Definitions
dataset_home = "./dataset"
datasrc_home = "./datasrc"
md5sums_file = "./datasrc/MD5SUMS"

# Dataset's datasrc
# Fields: dataset, srcfile
table = [
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2017-2018-08-01.csv.gz"]]

df = pd.DataFrame(table, columns='dataset srcfile'.split())

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

## Read MD5SUMS
try:
    with open(md5sums_file, 'r') as f:
        md5sums = pd.read_csv(md5sums_file, sep=' ', header=None,
                                names=['md5sum', 'lfilename'])

except FileNotFoundError:
    print('Error. Could open "{}". Run extract step first'.\
        format(md5sums_file))
    exit(-1)

## Build .parquet from .csv.gz

# 'Programas' dataset

programas = read_datasrc(datasrc_home + '/' + \
                           df[df['dataset'] == 'programas'].loc[0]['srcfile'],\
                           columns=True)
if not isinstance(programas, pd.DataFrame):
    print('ERROR, can\'t continue')
    exit(-1)

for i in df[df['dataset'] == 'programas']['srcfile']:
    programas = programas.append(read_datasrc(datasrc_home + '/' + i),\
                                    ignore_index=True)

print(programas.index)
print(programas.columns)

exit(0)

df = list()
for i in range(len(csv_files)):
    print(basedir + csv_files[i])
    df.append(pd.read_csv(basedir + csv_files[i], index_col=17, sep=';',encoding='iso-8859-1'))
    print("{} read.".format(csv_files[i]))

discentes = pd.concat(df)


# In[4]:


discentes.head()


# In[5]:


table = pa.Table.from_pandas(discentes) #, timestamps_to_ms=True)
pq.write_table(table, './dataset/br-capes-colsucup-discentes.parquet', compression='GZIP')

