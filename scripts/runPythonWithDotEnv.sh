#!/bin/bash
# file:         runPythonWithDotEnv.sh
# description:  allows to execute a python script received as first argument with previous eval of .env file"
# usage:        ./runPythonWithDotEnv.sh myscript.py
# dependencies: .env file in current directory

# let's test if an argument is passed
if [ -z "$1" ]; then
    echo "💥 💥️ Please provide the python script to run as first argument"
    exit 1
fi
SCRIPT=$1
#test if the argument is a python script
if [ "${SCRIPT: -3}" != ".py" ]; then
    echo "💥 💥️ Please provide a valid python script to run"
    exit 1
fi
#test if the .env file exists
if [ -f .env ]; then
    echo "# 👍👍 running python script ${SCRIPT} with .env file"
    set -a
    source .env
    set +a
    python "$SCRIPT"
else
    echo "# ⚠️⚠️ running python script ${SCRIPT} without .env file"
    python "$SCRIPT"
fi