# coding: utf-8
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

## Definitions
dataset_home = "./dataset"
datasrc_home = "./datasrc"

datasrc_table = [
 ["docentes",  "br-capes-colsucup-docentes.csv.gz"],
 ["discentes", "br-capes-colsucup-discentes.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv.gz"],
 ["programas", "br-capes-colsucup-prog-2017-2018-08-01.csv.gz"]]
src_df = pd.DataFrame(datasrc_table, columns='dataset srcfile'.split())

dataset_table = [
 ["docentes", "br-capes-docentes.parquet"],
 ["discentes", "br-capes-discentes.parquet"],
 ["programas", "br-capes-programas.parquet"]]
ds_df = pd.DataFrame(dataset_table, columns='dataset filename'.split())

programas_columns = ['CD_PROGRAMA_IES',
                    'AN_BASE',
                    'NM_GRANDE_AREA_CONHECIMENTO',
                    'NM_AREA_CONHECIMENTO',
                    'NM_SUBAREA_CONHECIMENTO',
                    'NM_ESPECIALIDADE',
                    'CD_AREA_AVALIACAO',
                    'NM_AREA_AVALIACAO',
                    'SG_ENTIDADE_ENSINO',
                    'NM_ENTIDADE_ENSINO',
                    'CS_STATUS_JURIDICO',
                    'DS_DEPENDENCIA_ADMINISTRATIVA',
                    'DS_ORGANIZACAO_ACADEMICA',
                    'NM_REGIAO',
                    'NM_MUNICIPIO_PROGRAMA_IES',
                    'SG_UF_PROGRAMA',
                    'NM_GRAU_PROGRAMA',
                    'CD_CONCEITO_PROGRAMA',
                    'ANO_INICIO_PROGRAMA',
                    'AN_INICIO_CURSO',
                    'IN_REDE',
                    'SG_ENTIDADE_ENSINO_REDE',
                    'DS_SITUACAO_PROGRAMA',
                    'DT_SITUACAO_PROGRAMA',
                    'ID_ADD_FOTO_PROGRAMA_IES',
                    'ID_ADD_FOTO_PROGRAMA',
                    'NM_PROGRAMA_IDIOMA']


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
        print('WARN. Couldn\'t open "{}".'.format(filename))
        return(-1)

## Main
for i in ds_df['dataset']:

    print('Reading "{}" CSV files.'.format(i))

    # Empty with columns dataframe
    if i == 'programas':
        df = pd.DataFrame(columns=programas_columns)
    else:
        df = read_datasrc(datasrc_home + '/' + \
                 src_df[src_df['dataset'] == i].iloc[0]['srcfile'],\
                 columns=True)

    if isinstance(df, pd.DataFrame):
        # Read CVS files
        for j in src_df[src_df['dataset'] == i]['srcfile']:
            df1 = read_datasrc(datasrc_home + '/' + j)
            df  = pd.concat([df,df1], join='inner', ignore_index=True)

        # Write parquet file
        pq_fname = dataset_home + '/' + \
              ds_df[ds_df['dataset'] == i].iloc[0]['filename']
        pq.write_table(pa.Table.from_pandas(df), pq_fname, compression='GZIP')

    else:
        print('WARN: "{}" parquet file will not be written.'.format\
                (dataset_home + '/' + \
                ds_df[ds_df['dataset'] == i].iloc[0]['filename']))
