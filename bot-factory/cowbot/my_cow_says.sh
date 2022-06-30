#!/bin/bash
my_cow=$(cowsay "$1")
#echo "$my_cow"
python3 cowsay.py "$my_cow"