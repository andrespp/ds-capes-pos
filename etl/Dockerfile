FROM continuumio/miniconda3
MAINTAINER Andre Pereira andrespp@gmail.com

RUN apt-get update && \
    apt-get install -y vim && \
    apt-get clean && rm -rf /var/lib/apt/list

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN conda install --yes --file requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
CMD ["help"]
