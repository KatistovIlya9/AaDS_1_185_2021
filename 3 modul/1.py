def z_fun(g):
    arr=[0]*len(g)
    l = r =0
    for i in range(1, len(g)):
        if i <= r:
            arr[i] = min(arr[i-l], r-i+1)
        while arr[i] + i < len(g) and g[arr[i]] == g[arr[i]+i]:
            arr[i] += 1
        if arr [i] + i - 1 > r:
            l=i
            r = arr[i] + i - 1
    return arr

def main():
    g = input()
    t = input()
    z = z_fun(t+"#" + g)
    for i in range(len(z)):
        if len(t) == z[i]:
            print(i- len(t) - 1, end = " ")

main()