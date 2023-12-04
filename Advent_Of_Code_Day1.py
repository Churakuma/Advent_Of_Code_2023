file = open("day1_part1_input.txt", "r")

sum = 0

for line in file: # Iterate through lines
    digits = []

    for char in line: # Iterate through characters
        if char.isdigit() == True: # Test if character is integer
            digits.append(char)
    print(digits)

    if len(digits) == 1:
        num = str(digits[0] + digits[0]) # Case where only one digit in line
    elif len(digits) > 1:
        num = str(digits[0] + digits[-1]) # Case where there is multiple digits in line
    else:
        continue # Skip if no digits in line
    sum += int(num)


print("The sum is: ", sum)