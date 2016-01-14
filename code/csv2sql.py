#!/usr/bin/python
# -*- coding: utf-8 -*-

from pharmacy import pharmacy

if __name__ == "__main__":
    import sys
    for l in open (sys.argv[1], "r").readlines():
        print pharmacy.fromCsv(l).sql()
