a = int(input('输入传送点个数:'))
b = int(input('输入朋友家位置:'))
i = 0
c = 0
n = 0
list1 = []
list2 = []
while i < a:
    c += 1
    h = int(input('传送门' + str(c) + '起始点:'))
    e = int(input('传送门' + str(c) + '结束点:'))
    i += 1
    list1.append(h)
    list2.append(e)
print('传送门起始位置：' + str(list1), '传送门结束位置：' + str(list2))
if list2[-1] >= b:
    print(list2[-1], b)
    if list1[0] == 0:
        print(list1[n+1])
        print(n)
        while n < a:
            if list2[n] > list1[n+1]:
                pass
                print(list2[n], list1[n+1])
            else:print('No')
            n += 1
    else:print('No')
else: print('No')