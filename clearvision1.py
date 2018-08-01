k, p = map(int, input().split())
list = []
i = 1
v = int()
R = 0
x = 0
s = 0
d = ''
c = ''
if k <= 100000:
    i = 1
    x = 1
    while i <= k:
        x = str(x)
        d = x[::-1]
        c = x + d
        c = int(c)
        list.append(c)
        x = int(x)
        x += 1
        i += 1
    for i in list:
        s += i
x = s % p
print(x)

