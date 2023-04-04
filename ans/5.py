# 5.

def print_max():
    
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    max = nums[0]
    
    print(max)

print_max()
