#!/bin/sh
if [ "$#" = "2" ]; then
    py ./src/LongestPath.py $1 $2
else
    py ./src/LongestPath.py
fi