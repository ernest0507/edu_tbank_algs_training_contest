# task 6
n = int(input())
nums = [int(x) for x in input().split()]

k = 0
i, j = 0, 0
for ind in range(n):
    if (nums[ind] % 2 == 0) != ((ind + 1) % 2 == 0):
        (i := ind) if k == 0 else (j := ind)
        k += 1

if k == 0 and n >= 3:
    print(1, 3)
elif (nums[i] % 2 + nums[j] % 2) != 1:
    print(-1, -1)
elif k == 2:
    print(i + 1, j + 1)
else:
    print(-1, -1)
