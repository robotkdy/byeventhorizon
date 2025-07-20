a,b,c = map(int,input().split())

def recu(k):
    if k == 1:
        return a % c
    r = recu(k//2)
    if k % 2 == 0:
        return r * r % c
    else:
        return (r*r)%c*a%c

print(recu(b))