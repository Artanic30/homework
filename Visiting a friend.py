n, m = map(int, input().split())
i = 0
c = 0
d = 1
list1 = []
list2 = []
Range = int()
while i < n:  #采集数据
    c += 1
    h, e = map(int, input().split())
    i += 1
    list1.append(h)
    list2.append(e)
if max(list2) >= m: # 最大值可能到达目标
    if list1[0] == 0:
        Range = list2[d-1]  #最大值范围
        while d <= n:
            if Range >= m: #触发范围超过目标
                print('yes')
                exit(0)
            elif Range >= list1[d] and Range <= list2[d]: #前进
                Range = list2[d]
                d += 1
            elif Range >= list1[d] and Range >= list2[d]:#停止
                d += 1
            else: #出错断层
                print('no')
                exit(0)
    else:
        print('No')
else:
    print('No')
