n,r,c = map(int,input().split())

def recu(y,x,l):
    if r < y and c < x:
        if l == 1:
            return 0
        else:
            return recu(y-l//2,x-l//2,l//2)
    elif r < y and c >= x:
        if l == 1:
            return 1
        else:
            return recu(y-l//2,x+l//2,l//2) + l * l
    elif r >= y and c < x:
        if l == 1:
            return 2
        else:
            return recu(y+l//2,x-l//2,l//2) + l * l *2
    elif r >= y and c >= x:
        if l == 1:
            return 3
        else:
            return recu(y+l//2,x+l//2,l//2) + l * l * 3

t = 2**n
print(recu(t//2,t//2,t//2))