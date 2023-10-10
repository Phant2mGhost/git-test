#list
numbers = [43, 54, 12, 67, 35, 20, 5, 9]
print("Numbers: " + str(numbers))
numbers_copy = numbers[:]
ascend = []
descend = []

#ascending
while len(numbers) != 0:
    first_1 = numbers[0]
    for n in numbers:
        if (n < first_1):
            first_1 = n
    numbers.remove(first_1)
    ascend.append(first_1)
    
#descending
while len(numbers_copy) != 0:
    first_2 = numbers_copy[0]
    for n in numbers_copy:
        if (n > first_2):
            first_2 = n
    numbers_copy.remove(first_2)
    descend.append(first_2)

#output
print("Ascending: " + str(ascend))
print("Descending: " + str(descend))    
