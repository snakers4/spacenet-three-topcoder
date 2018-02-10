#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--params', nargs = '*', dest = 'params', help = 'topcoder args', default = argparse.SUPPRESS)
    args = parser.parse_args()
    print(args.params[0])
