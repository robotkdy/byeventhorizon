import sys
input = sys.stdin.readline


n = int(input())
a = []

for _ in range(n):
    v = int(input())
    if v > 0:
        a.append(v)
    else:
        a.pop() #?
    

print(sum(a))