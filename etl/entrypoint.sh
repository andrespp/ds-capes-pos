#!/bin/bash

# Sets script to fail if any command fails.
set -e

datasrc() {
	echo Retrieving datasrc This may take a while. $@
	python extract.py
}

dataset() {
	echo Building dataset. $@
	python load.py
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
