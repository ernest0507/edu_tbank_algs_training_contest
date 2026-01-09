# task 5
l, r = [int(x) for x in input().split()]

count = 0
k = 0
for _ in range(18):
    k = k * 10 + 1
    for n in range(1, 10):
        count += l <= k * n <= r

print(count)
