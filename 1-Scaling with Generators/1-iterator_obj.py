numbers = [7, 4, 11, 3]
iter(numbers) # iterator_object

numbers_iter = iter(numbers)
for num in numbers_iter:
    print(num)