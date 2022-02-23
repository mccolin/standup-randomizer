#! /usr/bin/env python

"""
Standup Order Script -- randomizes order of subset lists

Usage: standup.py <list1> <list2> <list3> ...
  * "list" arguments are comma-separated strings

Example: standup.py Bugs,Daffy,Porky Foghorn,Sylvestre
"""

from sys import argv, exit
from random import sample

def bulleted(l, header=None):
    if header:
        print(header, f"\n{'-' * len(header)}")
    for p in l:
        print("*", p)

def randomize_list(l):
    return sample(l, len(l))


if len(argv) < 2:
    print("Usage: standup.py [GroupA:]MemberA,MemberB,MemberC [[GroupB:]Member1,Member2,Member3]")
    exit(1)

for arg in argv[1:]:
    if ":" in arg:
        group, people_str = arg.split(":")
    else:
        group = None
        people_str = arg

    people_list = randomize_list( people_str.split(",") )
    bulleted(people_list, header=group)
    print("")
