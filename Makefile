test:
	which docker
	which docker-compose
setup: docker-compose.yml etl/Dockerfile analysis/Dockerfile
	if [ ! -d dataset ] ; then mkdir dataset ; fi
	if [ ! -d datasrc ] ; then mkdir datasrc ; fi
	docker-compose pull
	docker-compose build

datasrc: datasrc/MD5SUMS etl/extract.py
	docker-compose run etl datasrc

dataset: etl/load.py
	docker-compose run etl dataset

seed:
	make datasrc
	make dataset
