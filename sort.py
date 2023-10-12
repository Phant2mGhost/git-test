import re
#user input
numbers = input('Numbers: ')
numbers = re.split(', |,|-| - |_| _ ', numbers)
print(numbers)
#str to in
numbers = [int(n) for n in numbers]
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
