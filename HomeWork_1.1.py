# Сформировать список из N членов последовательности.
# Для N = 5: 1,-3,9,-27,81
numbers = [1, 1, 1, 1, 1]
print(numbers)
N = 5
j = len(numbers)
for i in range(j):
    numbers[i]=((-3)**i)
print(numbers)
