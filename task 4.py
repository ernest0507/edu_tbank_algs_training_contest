# task 4
n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

diff_nums = [0]

for num in nums:
    length_num = len(str(num))
    for ind, ch in enumerate(str(num)):
        if int(ch) != 9:
            power = length_num - ind - 1
            diff_nums.append((9 - int(ch)) * 10 ** power)

print(sum(sorted(diff_nums, reverse=True)[:k]))
