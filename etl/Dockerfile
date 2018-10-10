#FROM python:3.7-alpine
FROM continuumio/miniconda3
MAINTAINER Andre Pereira andrespp@gmail.com

WORKDIR /usr/src/app

COPY ./requirements.txt ./

#RUN pip install --no-cache-dir -r requirements.txt
RUN conda install --yes --file requirements.txt

COPY . .

# Retrieve dataset
#RUN echo "Downloading CAPES Dataset. This may take a while." && \
#    rmdir $HOME/work && \
#    mkdir $HOME/datasrc $HOME/dataset $HOME/etl $HOME/analysis && \
#    cd $HOME/datasrc && \
#    wget -nv https://dadosabertos.capes.gov.br/dataset/903b4215-ea91-4927-8975-d1484891374f/resource/8b3464e2-9108-4855-bc5b-2df474fdf152/download/br-capes-colsucup-prog-2017-2018-08-01.csv && \
#    wget -nv https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/7de14e9c-9739-43d9-8217-ba9bf837b411/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv && \
#    wget -nv https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/a0c1760a-4130-49b7-b1fd-849ca189417b/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv && \
#    wget -nv https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/3c16cfcf-0614-4497-a3d4-324c0788fe2e/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv && \
#    wget -nv https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/bc2fb7a9-8313-4959-abee-14764d812e8b/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv && \
#    wget -nv https://dadosabertos.capes.gov.br/dataset/57f86b23-e751-4834-8537-e9d33bd608b6/resource/d918d02e-7180-4c7c-be73-980f9a8c09b5/download/br-capes-colsucup-docente-2017-2018-08-10.csv && \
#    gzip *.csv

#CMD ["python", "./etl.py"]
ENTRYPOINT ["./entrypoint.sh"]
CMD ["help"]
