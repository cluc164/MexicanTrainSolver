#!/bin/sh
if [ "$#" = "2" ]; then
    py LongestPath.py $1 $2
else
    py LongestPath.py
fi