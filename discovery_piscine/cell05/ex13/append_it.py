#!/usr/bin/env python3
import sys
import re

def main():
    args = sys.argv[1:]
    
    if not args:
        print("none")
        return
    
    for arg in args:
        if not re.search(r'ism$', arg):
            print(f"{arg}ism")
main()