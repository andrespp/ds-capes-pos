# coding: utf-8

# In[1]:
import pandas as pd
import hashlib


# ### Definitions

# In[2]:
datasrc_home = "./datasrc"
md5sums_file = "./datasrc/MD5SUMS"

## Library Functions
def md5(fname):
    hash_md5 = hashlib.md5()
    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except FileNotFoundError:
        return False

    return hash_md5.hexdigest()


# # Extract

# ### Dataset's resource list

# In[3]:


## Dataset's resource list:
# - Docentes da Pós-Graduação Stricto Sensu no Brasil de 2013 a 2016
# - Docentes da Pós-Graduação Stricto Sensu no Brasil 2017
# - Programas da Pós-Graduação Stricto Sensu do Brasil de 2013 a 2016
# - Programas da Pós-Graduação Stricto Sensu no Brasil 2017

# Fields: ds_name, ds_hash, resource_name, resource_hash, rfilename, download
#table = [["Docentes 2013 a 2016" , "35eab2f8-5a64-4619-b3f1-63a2e6690cfa", "2013", "3f5c3276-ff3a-496c-9250-b2cf87879e1f", "br-capes-colsucup-docente-2013a2016-2017-12-02_2013.csv", False],
         #["Docentes 2013 a 2016" , "35eab2f8-5a64-4619-b3f1-63a2e6690cfa", "2014", "0bd87bca-8202-4404-8628-73c92f29721d", "br-capes-colsucup-docente-2013a2016-2017-12-02_2014.csv", False],
         #["Docentes 2013 a 2016" , "35eab2f8-5a64-4619-b3f1-63a2e6690cfa", "2015", "75eea9d5-1542-4cfd-8ed9-d540d3eef344", "br-capes-colsucup-docente-2013a2016-2017-12-02_2015.csv", False],
         #["Docentes 2013 a 2016" , "35eab2f8-5a64-4619-b3f1-63a2e6690cfa", "2016", "922bc0d1-90eb-4939-9167-03831f732f72", "br-capes-colsucup-docente-2013a2016-2017-12-02_2016.csv", False],
         #["Docentes 2017"        , "57f86b23-e751-4834-8537-e9d33bd608b6", "2017", "d918d02e-7180-4c7c-be73-980f9a8c09b5", "br-capes-colsucup-docente-2017-2018-08-10.csv", False],
         #["Programas 2013 a 2016", "122620f6-47dc-4363-9d63-130c8a386af6", "2013", "7de14e9c-9739-43d9-8217-ba9bf837b411", "br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv", False],
         #["Programas 2013 a 2016", "122620f6-47dc-4363-9d63-130c8a386af6", "2014", "a0c1760a-4130-49b7-b1fd-849ca189417b", "br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv", False],
table =  [["Programas 2013 a 2016", "122620f6-47dc-4363-9d63-130c8a386af6", "2015", "3c16cfcf-0614-4497-a3d4-324c0788fe2e", "br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv", False],
         ["Programas 2013 a 2016", "122620f6-47dc-4363-9d63-130c8a386af6", "2016", "bc2fb7a9-8313-4959-abee-14764d812e8b", "br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv", False],
         ["Programas 2017"       , "903b4215-ea91-4927-8975-d1484891374f", "2017", "8b3464e2-9108-4855-bc5b-2df474fdf152", "br-capes-colsucup-prog-2017-2018-08-01.csv", False]]

# example url: https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/3f5c3276-ff3a-496c-9250-b2cf87879e1f/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2013.csv
df = pd.DataFrame(table, columns = 'ds_name ds_hash resource_name resource_hash rfilename download'.split())
df['url'] = 'https://dadosabertos.capes.gov.br/dataset/' + df['ds_hash'] +             '/resource/' + df['resource_hash'] +             "/download/" + df['rfilename']
df['filename'] = df['rfilename'].apply(lambda x: x.split(sep='.')[0]) #filename without extension

# ### Check MD5SUMS

# In[4]:


## Check if CSV file exists and is not corrupted

# Read MD5SUMS
try:
    with open(md5sums_file, 'r') as f:
        print("MD5SUMS file found! ")

        # read md5sum['md5sum', 'lfilename']
        md5sums = pd.read_csv(md5sums_file, sep=' ', header=None, names=['md5sum', 'lfilename'])

        # add md5sum['filename']
        md5sums['filename'] = md5sums['lfilename'].apply(lambda x: x.split(sep='.')[0]) #filename without extension

        # Compute MD5SUM of existing files
        # add md5sum['check']
        md5sums['check'] = md5sums['lfilename'].apply(lambda x: md5(datasrc_home + '/' + x))

        # add md5sum['corrupted']
        md5sums['corrupted'] = (md5sums['md5sum'] == md5sums['check']).apply(lambda x: not(x))

        # merge md5sums with df
        df = (pd.merge(df, md5sums[['corrupted', 'lfilename', 'filename', 'md5sum']], how='left', on='filename'))

        # set files to be downloaded - df['download']
        df ['download'] = (df['download'] | df['corrupted'])

except FileNotFoundError:

    print("MD5SUMS file not found. The whole dataset will be downloaded.")

    # set download to true
    df['download'] = df['download'].apply(lambda x: True)

    # add df['lfilename']
    df['lfilename'] = df['filename'] + ".csv.gz"

    # set df['md5sum']
    df['md5sum'] = df['filename'].apply(lambda x: 0)

# Cleanup df
df = df[['filename', 'lfilename', 'md5sum', 'url', 'download']]

# Define CSV files to be retrieved
to_retrieve = df[df['download'] == True]['url']


# ### CSV Download

# In[5]:


# Start ds retrieval
print("Need to download {} datasets.".format(len(to_retrieve)))
#for i in range(len(to_retrieve)):
for i in df[df['download'] == True].index:
    print('Retriveing "{}". '.format(df['filename'][i]), end="")

    resource_df = pd.read_csv(df['url'][i], index_col=17, sep=';',encoding='iso-8859-1')
    resource_df.to_csv(str(datasrc_home + "/" + df['lfilename'][i]), sep=';', compression='gzip')

    print('ok.')


# ### Update MD5SUMS

# In[6]:


# Compute new file's md5sum
df['md5sum'] = df['lfilename'].apply(lambda x: md5(datasrc_home + '/' + x))

# Write MD5SUMS
try:
    with open(md5sums_file, 'w') as f:
        df[['md5sum', 'lfilename']].to_csv(md5sums_file, sep=' ', header=None, index=False)
        print('Success. "{}" written'.format(md5sums_file))

except FileNotFoundError:

    print('Error. Could open "{}" for writing'.format(md5sums_file))
    exit(-1)


# # Transform

# # Load
