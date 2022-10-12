from unittest import result


nums_list = [22,37,58,29,87,90,300]

def get_numbers(nums):
    for num in nums:
        yield num

result = get_numbers(nums_list)
print(next(result))
print(next(result))
print(next(result))
print('I am exploring generator')
print(next(result))