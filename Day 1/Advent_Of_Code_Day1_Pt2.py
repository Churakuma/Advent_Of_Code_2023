import re

# Map numbers worded form to numerical form
number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def calculate_sum(data):
    sum = 0
    for i in range(len(data)):

        replace_words_with_numbers(i, data)
        data[i] = [extract_first_and_last_numbers(x) for x in data[i]]
        flattened_data = [item for sublist in data for item in sublist]
        number_to_add = flattened_data[i][0][0] + flattened_data[i][1][-1]
        sum += int(number_to_add)
    return sum

def extract_first_and_last_numbers(text):
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    if len(matches) == 1:
        return ((matches[0]), (matches[0]))
    elif len(matches) >= 2:
        return (matches[0]), (matches[-1])
    else:
        return None

def replace_words_with_numbers(i, data):
    for key in number_map:
        sublist = []
        # replacement adds the key back to either side of the number so that spelling is not broken on other number words
        replacement = key + str(number_map[key]) + key
        for x in data[i]:
            sublist.append(x.replace(key, replacement))
            data[i] = sublist

with open("day1_input.txt") as file:
    data = [x.strip().split(',') for x in file.read().splitlines()]


print(calculate_sum(data))