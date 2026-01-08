n, t = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
k = int(input())

l, r = nums[0], nums[-1]
if k - l <= t or r - k <= t:
    print(r - l)
else:
    print(r - l + min(k - l, r - k))
