from collections import deque

def dfs(n):

    for c in graph[n]:
        if vitsited[c] == False:
            vitsited[c] = True
            dfs(c)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

vitsited = [False] * (n+1)

q = deque()
q.append(1)
vitsited[1] = True
dfs(1)

#while q:
#    v = q.popleft()
#    for c in graph[v]:
#        if vitsited[c] == False:
#           q.append(c)
#            vitsited[c] = True

print(vitsited)