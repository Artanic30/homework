nums = list(map(int, input()[1:-1].split(",")))
i = len(nums)
x = 1
s1 = int()
s2 = int()
s = int()
list = []
b = 1
d = 1
min = int()
while d < len(list):
    if list[d - 1] <= list[d]:
        min = list[d - 1]
    else:
        min = list[d]
    d += 1
mask = min
while b <= i:
    a = 0
    while a + b <= i:
        for x in nums[a:a + b]:
            s1 += x
            x = 0
        if a + b == i:
            s2 = s1 - 1
        else:
            for x in nums[a + 1:a + b + 1]:
                s2 += x
                x = 0
        if s1 <= s2 and s2 >= mask:
           mask = s2
        else:
            pass
        a += 1
        s1 = 0
        s2 = 0
    list.append(mask)
    b += 1
while d < len(list):
    if list[d - 1] >= list[d]:
        mask = list[d - 1]
    else:
        mask = list[d]
    d += 1
print(mask)
