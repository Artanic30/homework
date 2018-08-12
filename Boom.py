N = int(input())
i = 1
dict = {}
while i <= N:
    n, m = map(int, input().split())
    dict[n] = m
print(dict)
