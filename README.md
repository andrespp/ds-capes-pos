capes pos dataset
==================

## Introdução

Dados de avaliação de programas de pós-graduação de instituições de ensino superior brasileiras.

## Origem dos dados
Dados públicos, disponibilidados pelo [Portal Dados Abertos](https://dadosabertos.capes.gov.br/) da [CAPES](https://www.capes.gov.br/).

Neste repositório, são utilizados dados referentes a [avaliação de programas de pós-graduação brasileiros](https://dadosabertos.capes.gov.br/organization/diretoria-de-avaliacao).

Em particular, os seguintes conjuntos de dados são considerados:
* [Informações de programas de pós-graduação](https://dadosabertos.capes.gov.br/organization/a994a478-5aaf-4e09-8372-134a0af7c0e8?groups=programas-pos-graduacao)
* [Docentes por programa](https://dadosabertos.capes.gov.br/organization/a994a478-5aaf-4e09-8372-134a0af7c0e8?groups=docentes)
* [Discentes matriculados e titulados](https://dadosabertos.capes.gov.br/organization/a994a478-5aaf-4e09-8372-134a0af7c0e8?groups=avaliacao-da-pos-graduacao)
* [Produção Intelectual Bibliográfica ](https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016)

## Conteúdo

Os _datasets_ utilizados neste repositório são os seguintes:

| #	| Desc			| Periodo | Link Capes | Link CSV |
| ----- | --------------------- | ------- | ---------- | -------- |
| 1	| Programas		| 2017	| [link][1] | [link][110] |
| 2	| Programas		| 2013	| [link][2] | [link][21] |
| 3	| Programas		| 2014	| [link][3] | [link][31] |
| 4	| Programas		| 2015	| [link][4] | [link][41] |
| 5	| Programas		| 2016	| [link][5] | [link][51] |
| 6	| Docentes		| 2017	| [link][6] | [link][61] |
| 7	| Docentes		| 2013	| [link][7] | [link][71] |
| 8	| Docentes		| 2014	| [link][8] | [link][81] |
| 9	| Docentes		| 2015	| [link][9] | [link][91] |
| 10	| Docentes		| 2016	| [link][10] | [link][101] |
| 11	| Discentes		| 2017	| [link][11] | [link][111] |
| 12	| Discentes		| 2013	| [link][12] | [link][121] |
| 13	| Discentes		| 2014	| [link][13] | [link][131] |
| 14	| Discentes		| 2015	| [link][14] | [link][141] |
| 15	| Discentes		| 2016	| [link][15] | [link][151] |
| 16	| Trabalhos em Anais	| 2013 a 2016 | [link][16] | [link][161] |
| 17	| Artigo em Jornal ou Revista	| 2013 a 2016 | [link][17] | [link][171] |
| 18	| Artigo em Periódico	| 2013 a 2016 | [link][18] | [link][181] |
| 19	| Livro			| 2014 a 2016 | [link][19] | [link][191] |


## Configuração do Ambiente

Os _datasets_ obtidos foram convertidos para uma base [PostgreSQL](https://www.postgresql.org/) utilizando a ferramenta de [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) Pentaho Data Integration ([PDI v7.1](https://sourceforge.net/projects/pentaho/files/Data%20Integration/7.1/)).

Para simplificar a implantação do serviço, foi criado uma solução via containers [Docker](https://www.docker.com/what-docker) contendo o servidor PostgreSQL e uma instância do [Pgadmin4](https://www.pgadmin.org/) (cliente)

### Requisitos

Distribuição Linux com as seguintes ferramentas instaladas:

* GIT
* Curl
* unzip
* Docker
* Docker Compose

### Clone do Repositório

```bash
$ git clone
```

### Obtenção do dataset

```bash
$ cd ds-ppgee-evaluation
$ cd dataset
$ # Download dataset
$ ./getDataset.sh
$ ls datasrc/
```

### Servidor PostgreSQL

```bash
$ cd ../compose
$ docker-compose up -d
```

### Carregamento da Base

Ajustar o arquivo `kettle.properties` de acordo com o servidor desejado (`localhost` é o padrão)

```bash
$ vim ../kettle.properties
```

Carregar a base

```bash
$ cd dw-pmoc
$ docker container run --rm -v $(pwd):/jobs andrespp/pdi \
	runj Jobs/load_dataset.kjb
```

## Utilizando o Dataset

Acesse o pgAdmin no seu navegador: `http://localhost`. Login: `user`, senha `pass`

Adicione o servidor da base: `Servers -> Create Server...`. Name: `localhost`, host `capesdb`, port `5432`, username `capesdb_user`, password `c4pes`

Selecione a base de dados `capesdb` e abra a ferramenta de consultas sql: `Tools -> Query Tool`

## References

* [Anuário estatístico da Previdência Social em 2015](http://www.previdencia.gov.br/wp-content/uploads/2015/08/AEPS-2015-FINAL.pdf)

[1](https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-programas-da-pos-graduacao-stricto-sensu-no-brasil-2017/resource/8b3464e2-9108-4855-bc5b-2df474fdf152)
[2](https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/7de14e9c-9739-43d9-8217-ba9bf837b411)
[3](https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/a0c1760a-4130-49b7-b1fd-849ca189417b)
[4](https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/3c16cfcf-0614-4497-a3d4-324c0788fe2e)
[5](https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/bc2fb7a9-8313-4959-abee-14764d812e8b)
[6](https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-docentes-da-pos-graduacao-stricto-sensu-no-brasil-2017/resource/d918d02e-7180-4c7c-be73-980f9a8c09b5)
[7](https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/3f5c3276-ff3a-496c-9250-b2cf87879e1f)
[8](https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/0bd87bca-8202-4404-8628-73c92f29721d)
[9](https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/75eea9d5-1542-4cfd-8ed9-d540d3eef344)
[10](https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/922bc0d1-90eb-4939-9167-03831f732f72)
[11](https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-discentes-da-pos-graduacao-stricto-sensu-do-brasil-2017/resource/2207af02-21f6-466e-a690-46f26a2804d6)
[12](https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/89bcb419-5a11-46a1-804e-e9df8e4e6097)
[13](https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/3aa223ba-9c60-421a-91af-48ed843a9a98)
[14](https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/08e7765f-cd76-4c7b-a29a-46e216dd79cf)
[15](https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/cfbcb060-d6af-4c34-baa7-16ef259273f7)
[16](https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/060d3c65-8024-49ee-a7f6-dc1710ff6513)
[17](https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/414b51bf-bbd8-4d6d-b1bb-ab5867167949)
[18](https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/e2c8a0e7-c473-467b-868f-f42d3c54aadd)
[19](https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/8d368433-8ab5-4a78-8f55-a7384d7dff18)

[110](https://dadosabertos.capes.gov.br/dataset/903b4215-ea91-4927-8975-d1484891374f/resource/8b3464e2-9108-4855-bc5b-2df474fdf152/download/br-capes-colsucup-prog-2017-2018-08-01.csv)
[21](https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/7de14e9c-9739-43d9-8217-ba9bf837b411/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv)
[31](https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/a0c1760a-4130-49b7-b1fd-849ca189417b/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv)
[41](https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/3c16cfcf-0614-4497-a3d4-324c0788fe2e/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv)
[51](https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/bc2fb7a9-8313-4959-abee-14764d812e8b/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv)
[61](https://dadosabertos.capes.gov.br/dataset/57f86b23-e751-4834-8537-e9d33bd608b6/resource/d918d02e-7180-4c7c-be73-980f9a8c09b5/download/br-capes-colsucup-docente-2017-2018-08-10.csv)
[71](https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/3f5c3276-ff3a-496c-9250-b2cf87879e1f/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2013.csv)
[81](https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/0bd87bca-8202-4404-8628-73c92f29721d/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2014.csv)
[91](https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/75eea9d5-1542-4cfd-8ed9-d540d3eef344/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2015.csv)
[101](https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/922bc0d1-90eb-4939-9167-03831f732f72/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2016.csv)
[111](https://dadosabertos.capes.gov.br/dataset/b7003093-4fab-4b88-b0fa-b7d8df0bcb77/resource/2207af02-21f6-466e-a690-46f26a2804d6/download/br-capes-colsucup-discentes-2017-2018-07-10.csv)
[121](https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/89bcb419-5a11-46a1-804e-e9df8e4e6097/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2013.csv)
[131](https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/3aa223ba-9c60-421a-91af-48ed843a9a98/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2014.csv)
[141](https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/08e7765f-cd76-4c7b-a29a-46e216dd79cf/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2015.csv)
[151](https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/cfbcb060-d6af-4c34-baa7-16ef259273f7/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2016.csv)
[161](https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/060d3c65-8024-49ee-a7f6-dc1710ff6513/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-anais.csv)
[171](https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/414b51bf-bbd8-4d6d-b1bb-ab5867167949/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-artjr.csv)
[181](https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/e2c8a0e7-c473-467b-868f-f42d3c54aadd/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-artpe.csv)
[191](https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/8d368433-8ab5-4a78-8f55-a7384d7dff18/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-livro.csv)
