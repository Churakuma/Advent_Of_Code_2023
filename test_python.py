def num_word_idx_from_file(file_path):
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

    with open(file_path, 'r') as file:
        total_sum = 0

        for line in file:
            indices = []

            for pat in patterns:
                for idx in range(len(line)):
                    if line.startswith(pat, idx):
                        indices.append((idx, patterns[pat]))

            if indices:
                if len(indices) == 1:
                    (left_i, left_val), (right_i, right_val) = indices[0], indices[0]
                else:
                    (left_i, left_val), (right_i, right_val) = indices[0], (0, 0)
            else:
                (left_i, left_val), (right_i, right_val) = (0, 0), (0, 0)

            for (idx, val) in indices[1:]:
                left = (idx, val) if idx < left_i else (left_i, left_val)
                right = (idx, val) if idx >= right_i else (right_i, right_val)

                left_i, left_val = left
                right_i, right_val = right

            print(str(left_val) + str(right_val))
            total_sum += left_val * 10 + right_val

    return total_sum

# Example usage:
file_path = "test_input.txt"  # Replace with the actual path to your file
result = num_word_idx_from_file(file_path)
print(result)