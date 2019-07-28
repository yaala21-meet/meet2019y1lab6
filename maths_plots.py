
def fibonacci(n):
    nums = [1, 1]
    for num in range(3,n+1):
        nums.append(nums[num-3]+nums[num-2])
    return nums[-1]

while True:
    my_input = int(input())
    print(fibonacci(my_input))
