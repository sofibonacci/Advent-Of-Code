import re

def recursive_search(expected_value, partial_result, line):
    if len(line) == 1:
        if expected_value == partial_result + line[0] or expected_value == partial_result * line[0]:
            return True
        return False

    first_number = line[0]
    remaining_line = line[1:]

    return (
        recursive_search(expected_value, partial_result + first_number, remaining_line) or
        recursive_search(expected_value, partial_result * first_number, remaining_line)
    )

def check_line_value(line):

    expected_value = line[0]
    numbers = line[1:] 

    initial_value = numbers[0]
    has_solution = recursive_search(expected_value, initial_value, numbers[1:])

    return expected_value if has_solution else 0

answer = 0
with open("7_actual_input.txt", "r") as problem_input:
    for line in problem_input:
        numbers = re.findall(r'\d+', line)
        numbers_list = list(map(int, numbers))
        print("line: ", numbers_list)
        answer += check_line_value(numbers_list)

print("answer is:", answer)