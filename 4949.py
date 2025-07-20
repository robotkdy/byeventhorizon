import sys
input = sys.stdin.readline

while True:
    
    s = input().rstrip()
    if s == ".":
        break
    l = []
    for c in s:
        if c == "(" or c == "[":
            l.append(c)
        elif c == ")" or c == "]":
            if len(l) == 0:
                l.append("ewjhdfs")
                break
            elif l[-1] == "(" and c == "]":
                break
            elif l[-1] == "[" and c == ")":
                break
            else:
                l.pop()
    if len(l) != 0:
        print("no")
    else:
        print("yes")