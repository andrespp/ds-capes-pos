import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

print("Hello World!")

df = pd.read_csv("/app/datasrc/br-capes-colsucup-discentes-2017-2018-07-10.csv.gz", \
                    index_col = 0,
                    compression='gzip',
                    sep=';',
                    encoding='iso-8859-1') #,
                    #error_bad_lines=False)

print("bla")
print(df.head())
