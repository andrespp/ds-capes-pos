test:
	which docker
	which docker-compose
setup:
	if [ ! -d dataset ] ; then mkdir dataset ; fi
	if [ ! -d datasrc ] ; then mkdir datasrc ; fi
	docker-compose pull
	docker-compose build

datasrc:
	docker-compose run etl datasrc

ds:
	docker-compose run etl dataset

seed:
	docker-compose run etl seed
