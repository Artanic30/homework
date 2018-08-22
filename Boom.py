import itertools

N = int(input())
i = 1
k = 1
s = 0
boxlist = []
zuhe = ()
color = set()
while i <= N:
    n_i, m_i = map(int, input().split())
    boxlist.append({m_i, n_i})
    while k <= len(boxlist):
        zuhe = itertools.combinations(boxlist, k)
        for a in zuhe:
            for b in a:
                for c in b:
                    color.add(c)
            if len(color) == k:
                print(i)
                exit(0)
            color = set()
        k += 1
    i += 1
    k = 1
print('no')

