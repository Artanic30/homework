n = int(input('输入传送点个数:'))
m = int(input('输入朋友家位置:'))
i = 0
c = 0
d = 1
list1 = []
list2 = []
while i < n:
    c += 1
    h = int(input('传送门' + str(c) + '起始点:'))
    e = int(input('传送门' + str(c) + '结束点:'))
    i += 1
    list1.append(h)
    list2.append(e)
# else:print('传送门起始位置：' + str(list1), '传送门结束位置：' + str(list2))
if list2[-1] >= m:
   # print(list2[-1], m)
    if list1[0] == 0:
      #  print(list1[d-1])
     #   print(list2[d])
     #   print(d)
        while d < n:
            # 1,2个条件限制后一个传送门起始位置在前一个门范围内3,限制后传送门为前进
            if list2[d-1] >= list1[d] and list2[d-1] >= list2[d]:
               print('no')
               exit(0)
            elif list2[d-1] <= list1[d] and list2[d-1] <= list2[d]:
                print('yes')
     #           print(d)
                d += 1
            else:exit(0)
    else:print('No')
else: print('No')