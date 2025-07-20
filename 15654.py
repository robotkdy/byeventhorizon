n,m = map(int, input().split())

l = list(map(int,input().split()))
l.sort()


ans = []

def recu(k):
    if len(ans) >= m:
        print(*ans)
        return
    for i in range(n):
        if l[i] == -1:
            continue
        ans.append(l[i])
        l[i] =-1
        recu(i+1)
        l[i] = ans.pop()
recu(0) 