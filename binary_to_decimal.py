import numpy as np                                
#user input into int list
def user_input():
    binary = []
    user_input = input("Binary Number: ")
    for b in user_input:
        b = int(b)
        binary.append(b)
    return binary

#checks for invalid input
def check_valid_input(binaries):
    for b in binaries:
        if b != 0 and b != 1:
            return False
    return True

binaries = user_input()

while not check_valid_input(binaries):
    print("Invalid input. Please enter binary number only.")
    binaries = user_input()

#int array multiplied by 2
num = np.array(binaries)
flip_num = num[::-1]
num_double = flip_num * 2

#convertion
list_len = len(flip_num)
i = 0
total = 0
while list_len > 0:
    for n in num_double:
        if n == 2:
            power = pow(n, i)
            i += 1
            total += power
            list_len -= 1
        elif n == 0:
            power = 0
            i += 1
            list_len -= 1
print("Decimal Number: " + str(total))
