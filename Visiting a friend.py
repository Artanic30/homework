a = int(input('输入传送点个数:'))
b = int(input('输入朋友家位置:'))
i = 0
c = 0
n = 1
list1 = []
list2 = []
while i < a:
    c += 1
    h = int(input('传送门' + str(c) + '起始点:'))
    e = int(input('传送门' + str(c) + '结束点:'))
    i += 1
    list1.append(h)
    list2.append(e)
# print('传送门起始位置：' + str(list1), '传送门结束位置：' + str(list2))
if list2[-1] >= b:
     #print(list2[-1], b)
    if list1[0] == 0:
       # print(list1[n-1])
       # print(list2[n])
       # print(n)
        while n < a:
            # 1,2个条件限制后一个传送门起始位置在前一个门范围内3,限制后传送门为前进
            if list2[n-1] >= list1[n]  and list1[n-1] < list1[n] and list2[n-1] < list2[n]:
                pass
                n += 1
            #print(n)
            else:break
        print('No')
        if n == a:
            print('Yes')
    else:print('No')
else: print('No')