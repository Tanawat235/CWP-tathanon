#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(keyword, text)
    count = len(matches)

    if count == 0:
        print("none")
    else:
        print(count)
main()