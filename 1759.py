from itertools import combinations


n,m = map(int, input().split())
s = input().split()
s.sort()

for st in combinations(s,n):
    j,m = 0,0
    for c in st:
        if c in 'aeiou':
            m += 1
        else:
            j += 1
    if j >= 2 and m >= 1:
        print(*st,sep= "")