import re

def determine_printability(line, rules, partial_answer):

    number_to_return = 0
    is_line_ok = False

    #base cases:
    if len(line) == 1:
        is_line_ok = True

    if len(line) == 2:
        is_line_ok = (rules[line[0]] == line[1])

    print(rules[line[0]])
        
    if len(line) == 3:      
        pass

    #if its printable, return the middle number
    
    if is_line_ok:
        number_to_return = 999

    return number_to_return



def extract_rules_from_file(file_name):
    rules = {}


    with open(file_name, 'r') as file:
        input_file_data = file.read().split('\n')  

    for lines in input_file_data:    
        numbers = re.findall(r'\d+', lines)
        rules_list = list(map(int, numbers))
        #print(rules_list)
        rules[rules_list[0]] = rules_list[1]
    
    #print(rules)
    return rules



def extract_printing_lists(file_name, rules):
    partial_answer = 0

    with open(file_name, 'r') as file:
        for line in file:
            line = list(map(int,  re.findall(r'\d+', line)))
            partial_answer += determine_printability(line, rules, partial_answer)
            #print(line)

        print(partial_answer)

extract_printing_lists("5_small_rows.txt", extract_rules_from_file("5_small_rules_input.txt"))