import re

with open("3_b_input.txt", "r") as problem_input:
    regex_input = problem_input.read()  # Read file content as a string

query = r"mul\((\d{1,3}),(\d{1,3})\)"

answer = 0

# Find all matches
matches = re.findall(query, regex_input)
print(matches)

# Transform matches to integers
int_matches = [(int(num1), int(num2)) for num1, num2 in matches]
print(int_matches)

# Calculate the answer
for match in int_matches:
    answer += (match[0] * match[1])
    print(answer)

# Final answer
print("Final answer:", answer)