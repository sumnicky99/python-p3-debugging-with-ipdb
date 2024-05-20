# lib/ipdb_debugging.py

import ipdb

def plus_two(num):
    num += 2
    ipdb.set_trace()  
    return num
