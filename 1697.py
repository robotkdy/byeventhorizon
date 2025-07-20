from collections import deque


n,k = map(int,input().split())

visited = [False] * 100_001

q = deque()

q.append((n,0))
visited[n] = True
while q:
    v,sec = q.popleft()
    if v == k:
        print(sec)
        break
    for nv in (v*2, v-1,v+1):
        if nv < 0 or nv > 100_000:
            continue
        if visited[nv] == False:
            visited[nv] = True
            q.append((nv,sec + 1))