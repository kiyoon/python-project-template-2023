#!/bin/bash

# Run all doctests in src/

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
for file in $(find $SCRIPT_DIR/../src/ -name "*.py"); do
	python3 -m doctest -v $file
done
