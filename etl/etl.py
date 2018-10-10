
# coding: utf-8

# In[1]:


import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd


# ### Load CSV files

# In[2]:


basedir = "./datasrc/"
#csv_files = ["br-capes-colsucup-discentes-2013a2016-2017-12-02_2013.csv", \
#                "br-capes-colsucup-discentes-2013a2016-2017-12-02_2014.csv", \
#                "br-capes-colsucup-discentes-2013a2016-2017-12-02_2015.csv", \
#                "br-capes-colsucup-discentes-2013a2016-2017-12-02_2016.csv", \
#                "br-capes-colsucup-discentes-2017-2018-07-10.csv"]
csv_files = ["br-capes-colsucup-docente-2017-2018-08-10.csv.gz"]


# In[3]:


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

