import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

print("Hello World!")
src = "br-capes-colsucup-docente-2017-2018-08-10.csv.gz"
df = pd.read_csv("./datasrc/" + src, \
                    index_col = 0,
                    compression='gzip',
                    sep=';',
                    encoding='iso-8859-1') #,
                    #error_bad_lines=False)

print("Dataset build. Sample:")
print(df.head())
