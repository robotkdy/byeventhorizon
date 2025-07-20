n,m = map(int, input().split())

l = list(map(int,input().split()))
l.sort()


ans = []

def recu(k):
    if len(ans) >= m:
        print(*ans)
        return
    for i in range(n):
        ans.append(l[i])
        recu(i+1)
        l[i] = ans.pop()
recu(0) 