#!/usr/bin/python3
import sys

f = open(sys.argv[2], 'wb')

with open(sys.argv[1], 'r') as lines:
        for line in lines:
            if not line.startswith('+'):
                f.write(bytes.fromhex(line))
f.close()
