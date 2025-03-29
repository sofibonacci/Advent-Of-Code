total_count = 0

def mas_or_sam_left_to_right(input_matrix, row_index, element_index):
    global total_count  

    if input_matrix[row_index][element_index] == 'M' and input_matrix[row_index + 1][element_index + 1] == 'A' and input_matrix[row_index + 2][element_index + 2] == 'S':
        return True
    if input_matrix[row_index][element_index] == 'S' and input_matrix[row_index+ 1][element_index + 1] == 'A' and input_matrix[row_index + 2][element_index + 2] == 'M':
        return True

    return False

def mas_or_sam_right_to_left(input_matrix, row_index, element_index):
    global total_count  
    
    if input_matrix[row_index][element_index] == 'M' and input_matrix[row_index + 1][element_index - 1] == 'A' and input_matrix[row_index + 2][element_index - 2] == 'S':
        return True
    if input_matrix[row_index][element_index] == 'S' and input_matrix[row_index + 1][element_index - 1] == 'A' and input_matrix[row_index + 2][element_index - 2] == 'M':
        return True

    return False

def search_star(input_matrix, row, row_index, element, element_index):
    global total_count  

    if mas_or_sam_left_to_right(input_matrix, row_index, element_index) and mas_or_sam_right_to_left(input_matrix, row_index, element_index + 2):
        total_count += 1

def solver(input_matrix):
    global total_count  

    for row_index, row in enumerate(input_matrix):
        for element_index, element in enumerate(row):
            if (row_index <= len(input_matrix) - 3) and (element_index <= len(row) - 3):
                search_star(input_matrix, row, row_index, element, element_index)

with open("4_real_input.txt", "r") as file:
    input_matrix = [list(line.strip()) for line in file]
    solver(input_matrix)
    print("total xmas counter is: ", total_count)