.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo
	@echo "Targets:"
	@echo "  test\t\tLookup for docker and docker-compose binaries"
	@echo "  help\t\tPrint this help"
	@echo "  setup\t\tCreate required directories and build docker images"
	@echo "  datasrc\tAttempt to download CSV source files"
	@echo "  dataset\tGenerate parquet files from CSV sources"
	@echo "  seed\t\tDownload CSV files and generate parquet files at once"

.PHONY: test
test:
	which docker
	which docker-compose

setup: docker-compose.yml etl/Dockerfile analysis/Dockerfile
	if [ ! -d dataset ] ; then mkdir dataset ; fi
	if [ ! -d datasrc ] ; then mkdir datasrc ; fi
	docker-compose pull
	docker-compose build

.PHONY: datasrc
datasrc: etl/extract.py
	docker-compose run -u $$(id -u) --rm etl datasrc

.PHONY: dataset
dataset: etl/load.py
	docker-compose run -u $$(id -u) --rm etl dataset

seed:
	make datasrc
	make dataset
