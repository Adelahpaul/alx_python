#!/usr/bin/python3
import sys


print(f"{len(sys.argv)} argument:")
for n in range(1, len(sys.argv)):
    print(f"{n}: {sys.argv[n]}")