from math import gcd


#Build
def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, do, a)
    build(2*v + 2, m, r, do, a)
    do[v] = gcd(do[2*v + 1], do[2*v + 2])

#Gcd
def get_gcd(v, l, r, do, ql, qr):
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_gcd(2*v+1, l, m, do, ql, qr)
    tr = get_gcd(2*v+2, m, r, do, ql, qr)
    return gcd(tl, tr)

#Update
def update(v, l, r, do, idx, value):
    if r-l == 1:
        do[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, do, idx, value)
    else:
        update(2*v+2, m, r, do, idx, value)
    do[v] = gcd(do[2*v + 1], do[2*v + 2])

#Main
def main():
    n = int(input())
    do = [0]*4*n
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, do, a)
    q = int(input())
    res = []
    while q != 0:
        que, l, r = map(str, input().split())
        if que=="s":
            res.append(get_gcd(0, 0, n, do, int(l)-1, int(r)))
        else:
            update(0, 0, n, do, int(l)-1, int(r))
        q -= 1
    print(*res)
main()
