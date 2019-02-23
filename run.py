#!/usr/bin/env python

import os
import sys

from sys import argv
from src.arg import process_args

if __name__ == '__main__':
    #check_database(Config.data())
    process_args(argv[1:])
    exit(0)
