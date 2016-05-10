#!/usr/bin/env bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$CURDIR

COMMAND="$1"

if [ "$COMMAND" = "run" ]
then
    python ./logger.py

elif [ "$COMMAND" = "test" ]
then
    python ./tests/simple_test.py

else
    echo "Command is unknown"
fi
