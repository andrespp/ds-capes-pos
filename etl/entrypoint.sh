#!/bin/bash

# Sets script to fail if any command fails.
set -e

datasrc() {
	echo Retrieving datasrc, may take a while $@
	cd datasrc/
	wget -nv https://dadosabertos.capes.gov.br/dataset/57f86b23-e751-4834-8537-e9d33bd608b6/resource/d918d02e-7180-4c7c-be73-980f9a8c09b5/download/br-capes-colsucup-docente-2017-2018-08-10.csv
	gzip -f *.csv

}

dataset() {
	echo Build dataset $@
	python etl.py
}

seed() {
	datasrc $@
	dataset $@
}

print_usage() {
echo "

Usage:	$0 COMMAND

ETL Container

Options:
  help		        Print this help
  datasrc		Retrieve datasrc
  dataset		Build dataset
  seed			Retrieve datasrc and build dataset
"
}

case "$1" in
    help)
        print_usage
        ;;
    datasrc)
	shift 1
        datasrc "$@"
        ;;
    dataset)
	shift 1
        dataset "$@"
        ;;
    seed)
	shift 1
        seed "$@"
        ;;
    *)
        exec "$@"
esac
