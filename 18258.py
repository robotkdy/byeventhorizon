import sys
input = sys.stdin.readline
from collections import deque


q = deque()

n = int(input())

for _ in range(n):
    s = input().split()
    if s[0] == "push":
        q.append(s[1])
    elif s[0] == "pop":
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif s[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])