test:
	which docker
	which docker-compose
setup:
	if [ ! -d dataset ] ; then mkdir dataset ; fi
	if [ ! -d datasrc ] ; then mkdir datasrc ; fi
	docker-compose pull
	docker-compose build

extract: etl/entrypoint.sh
	docker-compose run etl datasrc

dataset: etl/etl.py
	docker-compose run etl dataset

seed:
	docker-compose run etl seed
