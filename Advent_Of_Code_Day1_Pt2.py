file = open("test_input.txt", "r")
sum = 0

patterns = {
        "one": 1, "1": 1,
        "two": 2, "2": 2,
        "three": 3, "3": 3,
        "four": 4, "4": 4,
        "five": 5, "5": 5,
        "six": 6, "6": 6,
        "seven": 7, "7": 7,
        "eight": 8, "8": 8,
        "nine": 9, "9": 9,
        # Add more patterns as needed
    }

for line in file:
    indices = []

    for pattern in patterns:
        for index in range(len(line)):
            if line.startswith(pattern, index):
                indices.append((index, patterns[pattern]))

if indices:
    if len(indices) == 1:
        (left_index, left_value), (right_index, right_value) = indices[0], indices[0]
    else:
        (left_index, left_value), (right_index, right_value) = indices[0], (0, 0)
else:
    (left_index, left_value), (right_index, right_value) = (0, 0), (0, 0)
