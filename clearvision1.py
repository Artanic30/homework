n, m = map(int, input().split())
i = 0
c = 0
d = 1
list1 = []
list2 = []
Range = int()
while i < n:
    c += 1
    h, e = map(int, input().split())
    i += 1
    list1.append(h)
    list2.append(e)
if max(list2) >= m:
    if list1[0] == 0:
        Range = list2[d-1]
        while d <= n:
            if Range >= m:
                print('yes')
                exit(0)
            elif Range >= list1[d] and Range <= list2[d]:
                Range = list2[d]
                d += 1
            elif Range >= list1[d] and Range >= list2[d]:
                d += 1
            else:
                print('no')
                exit(0)
    else:
        print('No')
else:
    print('No')
