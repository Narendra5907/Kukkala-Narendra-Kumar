numbers = input("Enter numbers: ")
nums = list(map(int, numbers.split(',')))
result = {}
for i in range(1, 10):
    count = 0
    for n in nums:
        if n % i == 0:
            count += 1
    result[i] = count
print(result)