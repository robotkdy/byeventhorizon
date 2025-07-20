n = int(input())
ans = []
def recu(st,md,end,n):
    if n == 1:
        ans.append((st,end))
        return
    recu(st,end,md,n-1)
    ans.append((st,end))
    recu(md,st,end,n-1)
recu(1,2,3,n)
print(len(ans))
for a in ans:
    print(*a)