import re
from decimal import Decimal, getcontext
#to improve precision
getcontext().prec = 70

def calculate_price(A_X, A_Y, B_X, B_Y, P_X, P_Y):
    A_X = Decimal(A_X)
    A_Y = Decimal(A_Y)
    B_X = Decimal(B_X)
    B_Y = Decimal(B_Y)
    P_X = Decimal(P_X)
    P_Y = Decimal(P_Y)

#added in part b)
    P_X += 10000000000000
    P_Y += 10000000000000

#this is the general solution done with MATH on paper - for once proven useful
    a = (P_Y - P_X / B_X * B_Y) / (A_Y - A_X / B_X * B_Y)
    b = (P_Y - P_X / A_X * A_Y) / (B_Y - B_X / A_X * A_Y)

    print(repr(a),repr(b))

    if (-0.0000001 <= (a - round(a)) <= 0.0000001) and (-0.0000001 <= (b - round(b)) <= 0.0000001):
        return 3 * (round(a)) + round(b)
    return(0) #don't do this at home kiddo

def extract_numbers_from_file(file_name):
    total_price = 0
    with open(file_name, 'r') as file:
        input_file_data = file.read().split('\n\n')
        print(input_file_data)
    
    claw_machine_numbers = []

    for lines in input_file_data:    
        numbers = re.findall(r'\d+', lines)
        claw_machine_numbers = list(map(int, numbers))
        print(claw_machine_numbers)
        total_price += calculate_price(*claw_machine_numbers)

    print(total_price)

extract_numbers_from_file("13_actual_input.txt")