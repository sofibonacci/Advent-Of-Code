import re

def recursive_search(expected_value, partial_result, line):
    # Base case: if the line has only one number left
    if len(line) == 1:
        # Check if either addition or multiplication satisfies the expected value
        if expected_value == partial_result + line[0]:
            return True
        if expected_value == partial_result * line[0]:
            return True
        return False

    # Recursive case: try addition and multiplication with the first number
    first_num = line[0]
    remaining_line = line[1:]  # Avoid modifying the original list

    # Try addition and multiplication
    if recursive_search(expected_value, partial_result + first_num, remaining_line):
        return True
    if recursive_search(expected_value, partial_result * first_num, remaining_line):
        return True

    # Try concatenation of adjacent numbers in the list
    for i in range(len(line) - 1):
        # Concatenate line[i] and line[i+1]
        concatenated = int(str(line[i]) + str(line[i+1]))
        new_line = line[:i] + [concatenated] + line[i + 2:]
        if recursive_search(expected_value, partial_result, new_line):
            return True

    return False

def check_line_value(line):
    # Save expected value and the remaining numbers
    expected_value = line[0]
    numbers = line[1:]  # Rest of the line

    # Start recursion with the first number in the line
    if len(numbers) < 2:
        return 0  # If there are not enough numbers, return 0

    initial_value = numbers[0]
    has_solution = recursive_search(expected_value, initial_value, numbers[1:])

    # If there's at least one solution, add the expected value once
    return expected_value if has_solution else 0

answer = 0
with open("7_actual_input.txt", "r") as problem_input:
    for line in problem_input:
        numbers = re.findall(r'\d+', line)
        numbers_list = list(map(int, numbers))
        print("Processing line:", numbers_list)
        answer += check_line_value(numbers_list)

print("Final answer is:", answer)

# 4998764814652 -> TOO LOW. also, took literraly 2 hours to run.
# TODO: eliminate recursion.