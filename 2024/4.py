total_count = 0

def is_left_to_right_horizontal_xmas(line, index):
    return line[index] == 'X' and line[index + 1] == 'M' and line[index + 2] == 'A' and line[index + 3] == 'S'

def is_right_to_left_horizontal_samx(line, index):
    return line[index] == 'S' and line[index + 1] == 'A' and line[index + 2] == 'M' and line[index + 3] == 'X'


def search_in_horizonal_line(line):
    global total_count
    for index in range(len(line) - 3):
        if is_left_to_right_horizontal_xmas(line, index):
            total_count += 1
            print("there is an xmas")
        if is_right_to_left_horizontal_samx(line, index):
            total_count += 1
            print("there is a samx")

def search_top_left_to_bottom_right(input_matrix, row, row_index, element, element_index):
    global total_count  
         
    if input_matrix[row_index][element_index] == 'X' and input_matrix[row_index + 1][element_index + 1] == 'M' and input_matrix[row_index + 2][element_index + 2] == 'A' and input_matrix[row_index + 3][element_index + 3] == 'S':
        total_count += 1
        print("there is a top-left to bottom-right XMAS")

    if input_matrix[row_index][element_index] == 'S' and input_matrix[row_index + 1][element_index + 1] == 'A' and input_matrix[row_index + 2][element_index + 2] == 'M' and input_matrix[row_index + 3][element_index + 3] == 'X':
        total_count += 1
        print("there is a top-left to bottom-right SAMX")

def search_top_right_to_bottom_left(input_matrix, row, row_index, element, element_index):
    global total_count   
    
    if input_matrix[row_index][element_index] == 'X' and input_matrix[row_index + 1][element_index -1] == 'M' and input_matrix[row_index + 2][element_index - 2] == 'A' and input_matrix[row_index + 3][element_index - 3] == 'S':
        total_count += 1
        print("there is a top-right to bottom-left XMAS")

    if input_matrix[row_index][element_index] == 'S' and input_matrix[row_index + 1][element_index -1] == 'A' and input_matrix[row_index + 2][element_index - 2] == 'M' and input_matrix[row_index + 3][element_index - 3] == 'X':
        total_count += 1
        print("there is a top-right to bottom-left SAMX")

def search_vertical(input_matrix, row, row_index, element, element_index):
    global total_count   
    
    if input_matrix[row_index][element_index] == 'X' and input_matrix[row_index + 1][element_index] == 'M' and input_matrix[row_index + 2][element_index] == 'A' and input_matrix[row_index + 3][element_index] == 'S':
        total_count += 1
        print("there is a vertical XMAS")

    if input_matrix[row_index][element_index] == 'S' and input_matrix[row_index + 1][element_index] == 'A' and input_matrix[row_index + 2][element_index] == 'M' and input_matrix[row_index + 3][element_index] == 'X':
        total_count += 1
        print("there is a vertical SAMX")

def solver(input_matrix):
    for row_index, row in enumerate(input_matrix):
        search_in_horizonal_line(row)
        for element_index, element in enumerate(row):
            if row_index <= len(input_matrix) - 4:
                search_vertical(input_matrix, row, row_index, element, element_index)
            if (row_index <= len(input_matrix) - 4) and (element_index <= len(row) - 4):
                search_top_left_to_bottom_right(input_matrix, row, row_index, element, element_index)
            if (row_index <= len(input_matrix) - 4) and (element_index >= 3):
                search_top_right_to_bottom_left(input_matrix, row, row_index, element, element_index)
                    
with open("4_real_input.txt", "r") as file:
    # convert each line into a list of characters
    input_matrix = [list(line.strip()) for line in file]
    solver(input_matrix)
    print("total xmas counter is: ", total_count)