#!/usr/bin/env python3 
import os


SPLIT_FILE = 'SPLIT/list.txt'
SPLIT_OUTPUT = 'INPUT/list_'
SPLIT_LINES = 10

check_file = os.path.isfile(SPLIT_FILE)
if check_file:
    os.system(f'split -l {SPLIT_LINES} -d {SPLIT_FILE} {SPLIT_OUTPUT}')
    print("Split to INPUT")
else:
    print("SPLIT/list.txt non-exist")