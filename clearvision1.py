k, p = map(int, input().split())
list = []
i = 1
v = int()
R = 0
x = 0
s = 0
d = ''
c = ''
if k <= 9:
     while i <= k:
        v = 11*i
        list.append(v)
        i += 1
     for i in list:
         s += i
#     print(s)
elif 10 <= k <= 99:
    i = 10
    x = 10
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
    s += 495
elif 100 <= k <= 999:
    i = 100
    x = 100
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
    s += 495495
elif 1000 <= k <= 9999:
    i = 1000
    x = 1000
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
    s += 495495495
elif 10000 <= k <= 19999:
    i = 10000
    x = 10000
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
    s += 495495495495
elif 20000 <= k <= 29999:
    i = 20000
    x = 20000
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
    s += 15495495455495
elif 30000 <= k <= 39999:
    i = 30000
    x = 30000
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
    s += 40495495425495
elif 40000 <= k <= 49999:
    i = 40000
    x = 40000
    while i <= k:
        x = str(x)
        d = x[::-1]
        c = x + d
        c = int(c)
        list.append(c)
        x = int(x)
        x += 1
        i += 1
    for z in list:
        s += z
    s += 75495495405495
elif 50000 <= k <= 59999:
    i = 50000
    x = 50000
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
    s += 120495495395495
elif 60000 <= k <= 69999:
    i = 60000
    x = 60000
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
    s += 175495495395495
elif 70000 <= k <= 79999:
    i = 70000
    x = 70000
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
    s += 240495495405495
elif 80000 <= k <= 89999:
    i = 80000
    x = 80000
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
    s += 315495495425495
elif 90000 <= k <= 99999:
    i = 90000
    x = 90000
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
    s += 400495495455495
else:
    s = 100000000001 + 495495495495495
x = s % p
print(x)

