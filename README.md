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
* [Produção Intelectual Bibliográfica ](https://dadosabertos.capes.gov.br/organization/a994a478-5aaf-4e09-8372-134a0af7c0e8?groups=producao-intelectual-da-pos-graduacao)

## Conteúdo

Os _datasets_ utilizados neste repositório são os seguintes:

| #	| Desc			| Periodo | Link Capes | Link CSV |
| ----- | --------------------- | ------- | ---------- | -------- |
| 1	| Programas		| 2017	| [link][p1] | [link][p110] |
| 2	| Programas		| 2013	| [link][p2] | [link][p21] |
| 3	| Programas		| 2014	| [link][p3] | [link][p31] |
| 4	| Programas		| 2015	| [link][p4] | [link][p41] |
| 5	| Programas		| 2016	| [link][p5] | [link][p51] |
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
| 20	| Trabalhos em Anais	| 2017 | [link][20] | [link][201] |
| 21	| Artigo em Jornal ou Revista	| 2017 | [link][21] | [link][211] |
| 22	| Artigo em Periódico	| 2017 | n/d | n/d |
| 23	| Livro			| 2017 | [link][23] | [link][231] |


## Configuração do Ambiente

O _dataset_ e baixado e convertido automaticamente em arquivos parquet através da imagem docker do projeto.

A imagem dispõe ainda de ambiente jupyter notebook, onde é possível acessar as análises realizadas.

### Requisitos

Distribuição Linux com as seguintes ferramentas instaladas:

* Docker
* Docker Compose

### Clone do Repositório

```bash
$ git clone https://github.com/andrespp/ds-capes-pos.git
```

### Obtenção do dataset

O  _build_ da imagem irá baixar o _dataset_ e converter em arquivos parquet.

```bash
$ make setup
$ make seed
```

### Análises

Jupyter notebook

```bash
$ docker-compose up
```


## References

* [Portal dados abertos - Capes](https://dadosabertos.capes.gov.br/)

[p1]: https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-programas-da-pos-graduacao-stricto-sensu-no-brasil-2017/resource/8b3464e2-9108-4855-bc5b-2df474fdf152
[p2]: https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/7de14e9c-9739-43d9-8217-ba9bf837b411
[p3]: https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/a0c1760a-4130-49b7-b1fd-849ca189417b
[p4]: https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/3c16cfcf-0614-4497-a3d4-324c0788fe2e
[p5]: https://dadosabertos.capes.gov.br/dataset/programas-da-pos-graduacao-stricto-census-do-brasil-de-2013-a-2015/resource/bc2fb7a9-8313-4959-abee-14764d812e8b
[6]: https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-docentes-da-pos-graduacao-stricto-sensu-no-brasil-2017/resource/d918d02e-7180-4c7c-be73-980f9a8c09b5
[7]: https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/3f5c3276-ff3a-496c-9250-b2cf87879e1f
[8]: https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/0bd87bca-8202-4404-8628-73c92f29721d
[9]: https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/75eea9d5-1542-4cfd-8ed9-d540d3eef344
[10]: https://dadosabertos.capes.gov.br/dataset/docentes-posgraduacao/resource/922bc0d1-90eb-4939-9167-03831f732f72
[11]: https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-discentes-da-pos-graduacao-stricto-sensu-do-brasil-2017/resource/2207af02-21f6-466e-a690-46f26a2804d6
[12]: https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/89bcb419-5a11-46a1-804e-e9df8e4e6097
[13]: https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/3aa223ba-9c60-421a-91af-48ed843a9a98
[14]: https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/08e7765f-cd76-4c7b-a29a-46e216dd79cf
[15]: https://dadosabertos.capes.gov.br/dataset/discentes-da-pos-graduacao-stricto-sensu-do-brasil/resource/cfbcb060-d6af-4c34-baa7-16ef259273f7
[16]: https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/060d3c65-8024-49ee-a7f6-dc1710ff6513
[17]: https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/414b51bf-bbd8-4d6d-b1bb-ab5867167949
[18]: https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/e2c8a0e7-c473-467b-868f-f42d3c54aadd
[19]: https://dadosabertos.capes.gov.br/dataset/detalhes-da-producao-intelectual-bibliografica-2013a2016/resource/8d368433-8ab5-4a78-8f55-a7384d7dff18
[20]: https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-producao-intelectual-de-programas-de-pos-graduacao-stricto-sensu-no-brasil-de-2017/resource/b93739f0-0bcd-48c7-ae8a-78ae417656c7
[201]: https://dadosabertos.capes.gov.br/dataset/a93eaa05-5787-46ea-9997-fd970b718a41/resource/b93739f0-0bcd-48c7-ae8a-78ae417656c7/download/br-capes-colsucup-producao-2017a2018-2018-08-20-bibliografica-anais.csv
[21]: https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-producao-intelectual-de-programas-de-pos-graduacao-stricto-sensu-no-brasil-de-2017/resource/04a8c9bb-a123-4b4c-92dd-c242d67c9e5f
[211]: https://dadosabertos.capes.gov.br/dataset/a93eaa05-5787-46ea-9997-fd970b718a41/resource/04a8c9bb-a123-4b4c-92dd-c242d67c9e5f/download/br-capes-colsucup-producao-2017a2018-2018-08-20-bibliografica-artjr.csv
[23]: https://dadosabertos.capes.gov.br/dataset/coleta-de-dados-producao-intelectual-de-programas-de-pos-graduacao-stricto-sensu-no-brasil-de-2017/resource/da052cbe-64d6-41fd-a1b0-9ad555d10d61
[231]: https://dadosabertos.capes.gov.br/dataset/a93eaa05-5787-46ea-9997-fd970b718a41/resource/da052cbe-64d6-41fd-a1b0-9ad555d10d61/download/br-capes-colsucup-producao-2017a2018-2018-08-20-bibliografica-livro.csv
[p110]: https://dadosabertos.capes.gov.br/dataset/903b4215-ea91-4927-8975-d1484891374f/resource/8b3464e2-9108-4855-bc5b-2df474fdf152/download/br-capes-colsucup-prog-2017-2018-08-01.csv
[p21]: https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/7de14e9c-9739-43d9-8217-ba9bf837b411/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2013.csv
[p31]: https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/a0c1760a-4130-49b7-b1fd-849ca189417b/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2014.csv
[p41]: https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/3c16cfcf-0614-4497-a3d4-324c0788fe2e/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2015.csv
[p51]: https://dadosabertos.capes.gov.br/dataset/122620f6-47dc-4363-9d63-130c8a386af6/resource/bc2fb7a9-8313-4959-abee-14764d812e8b/download/br-capes-colsucup-prog-2013a2016-2017-12-02_2016.csv
[61]: https://dadosabertos.capes.gov.br/dataset/57f86b23-e751-4834-8537-e9d33bd608b6/resource/d918d02e-7180-4c7c-be73-980f9a8c09b5/download/br-capes-colsucup-docente-2017-2018-08-10.csv
[71]: https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/3f5c3276-ff3a-496c-9250-b2cf87879e1f/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2013.csv
[81]: https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/0bd87bca-8202-4404-8628-73c92f29721d/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2014.csv
[91]: https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/75eea9d5-1542-4cfd-8ed9-d540d3eef344/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2015.csv
[101]: https://dadosabertos.capes.gov.br/dataset/35eab2f8-5a64-4619-b3f1-63a2e6690cfa/resource/922bc0d1-90eb-4939-9167-03831f732f72/download/br-capes-colsucup-docente-2013a2016-2017-12-02_2016.csv
[111]: https://dadosabertos.capes.gov.br/dataset/b7003093-4fab-4b88-b0fa-b7d8df0bcb77/resource/2207af02-21f6-466e-a690-46f26a2804d6/download/br-capes-colsucup-discentes-2017-2018-07-10.csv
[121]: https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/89bcb419-5a11-46a1-804e-e9df8e4e6097/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2013.csv
[131]: https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/3aa223ba-9c60-421a-91af-48ed843a9a98/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2014.csv
[141]: https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/08e7765f-cd76-4c7b-a29a-46e216dd79cf/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2015.csv
[151]: https://dadosabertos.capes.gov.br/dataset/dc2568b7-20b0-4d92-980d-dcf2485b5517/resource/cfbcb060-d6af-4c34-baa7-16ef259273f7/download/br-capes-colsucup-discentes-2013a2016-2017-12-02_2016.csv
[161]: https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/060d3c65-8024-49ee-a7f6-dc1710ff6513/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-anais.csv
[171]: https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/414b51bf-bbd8-4d6d-b1bb-ab5867167949/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-artjr.csv
[181]: https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/e2c8a0e7-c473-467b-868f-f42d3c54aadd/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-artpe.csv
[191]: https://dadosabertos.capes.gov.br/dataset/6adc0781-4314-4703-9c87-0c86ccec09c1/resource/8d368433-8ab5-4a78-8f55-a7384d7dff18/download/br-colsucup-prod-detalhe-bibliografica-2013a2016-2017-10-01-livro.csv
