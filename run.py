#!/usr/bin/env python

import os
import sys

from sys import argv
from src.arg import process_args
from src.context import Context

if __name__ == '__main__':
    Context.set('APP_ROOT', os.path.dirname(os.path.abspath(__file__)))
    Context.set('APP_DIR',  Context.get('APP_ROOT'))
    Context.set('DATA_DIR', "%s/data" % Context.get('APP_DIR'))
    process_args(argv[1:])
    exit(0)
