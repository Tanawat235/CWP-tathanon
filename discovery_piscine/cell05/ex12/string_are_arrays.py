#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    
    if len(args) != 1:
        print("none")
        return
    
    text = args[0]
    
    z_list = [char for char in text if char == 'z']
    
    if not z_list:
        print("none")
    else:
        print("".join(z_list))
main()