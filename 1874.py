import sys
input = sys.stdin.readline

n = int(input())
l = []
t = []
for _ in range(n):
    t.append(int(input()))

idx = 0
ans = []

for num in range(1,n+1):
    l.append(num)
    ans.append("+")
    while l and l[-1] == t[idx]:
        l.pop()
        idx += 1
        ans.append("-")

if len(l) == 0:
    print(*ans, sep= "\n")
else:
    print("NO")