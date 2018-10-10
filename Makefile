test:
	which docker
	which docker-compose
setup:
	docker-compose pull
	docker-compose build
	make seed

seed:
	echo bla
