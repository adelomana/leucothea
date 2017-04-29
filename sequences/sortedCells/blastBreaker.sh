#!/bin/bash

# this script breaks into 2 files the original DIAMOND output file

# wc -l 04-124-big-cells.strict.m8
# 973465652 04-124-big-cells.strict.m8

time head -n 486732826 /Users/alomana/scratch/sortedCells/diamond/04-124-big-cells.strict.m8 > /Users/alomana/scratch/sortedCells/diamond/04-124-big-cells.strict.a.m8

time tail -n +486732827 /Users/alomana/scratch/sortedCells/diamond/04-124-big-cells.strict.m8 > /Users/alomana/scratch/sortedCells/diamond/04-124-big-cells.strict.b.m8
