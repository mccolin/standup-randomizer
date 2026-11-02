#! /usr/bin/env python

"""
Standup Order Script -- randomizes order of subset lists

Usage: standup.py [--popcorn] <list1> <list2> <list3> ...
  * "list" arguments are comma-separated strings
  * --popcorn pauses after each name until Enter is pressed

Example: standup.py Bugs,Daffy,Porky Foghorn,Sylvestre
"""

from sys import argv, exit
from random import sample

def bulleted(l, header=None, popcorn=False, counter=None):
    if header:
        print(header, f"\n{'-' * len(header)}")
    for p in l:
        if popcorn:
            counter["current"] += 1
            print("*", p, f"({counter['current']}/{counter['total']})", end="")
            if counter["current"] < counter["total"]:
                input()
            else:
                print()
        else:
            print("*", p)

def randomize_list(l):
    return sample(l, len(l))


args = argv[1:]
popcorn = "--popcorn" in args
args = [a for a in args if a != "--popcorn"]

if len(args) < 1:
    print("Usage: standup.py [--popcorn] [GroupA:]MemberA,MemberB,MemberC [[GroupB:]Member1,Member2,Member3]")
    exit(1)

groups = []
for arg in args:
    if ":" in arg:
        group, people_str = arg.split(":")
    else:
        group = None
        people_str = arg
    groups.append((group, randomize_list(people_str.split(","))))

counter = {"current": 0, "total": sum(len(people) for _, people in groups)}

try:
    for group, people_list in groups:
        bulleted(people_list, header=group, popcorn=popcorn, counter=counter)
        print("")
except (KeyboardInterrupt, EOFError):
    print()
    exit(0)
