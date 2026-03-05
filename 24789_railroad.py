import sys

x,y = map(int, sys.stdin.readline().split())
if y % 2 == 0:
    print("possible")
else:
    print("impossible")
