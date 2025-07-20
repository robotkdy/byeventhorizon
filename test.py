def r(n):
    if n == 0:
        return
    r(n-1)
    print(n)

r(10)