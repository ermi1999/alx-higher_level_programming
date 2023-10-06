#!/usr/bin/python3
import sys
arg_len = len(sys.argv) - 1
j = 1
if arg_len == 0:
    print("{} argumnts.".format(arg_len))
elif arg_len == 1:
    print("{} argument:".format(arg_len))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(arg_len))
    for i in sys.argv[1:]:
        argument = sys.argv[j]
        print("{}: {}".format(j, argument))
        j += 1
