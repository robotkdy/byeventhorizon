from collections import deque


q = deque()

n = int(input())

for num in range(1,n+1):
    q.append(num)
    print(q)
while len(q) > 1:
    q.pop()
    q.append(q[0])
    q.pop()
    print(q)
print(*q)