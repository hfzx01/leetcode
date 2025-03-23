n = int(input())
a = list(map(int, input().split()))
result = 0
def increase(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True
for i in range(n+1):
    for j in range(i+1, n+1):
        if increase(a[:i]+a[j:]):
            result += 1
print(result)
