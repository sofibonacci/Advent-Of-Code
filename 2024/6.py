import sys

#if I don't do this python gives up
sys.setrecursionlimit(7000)

def find_starting_position(maze):
    for row_index, row in enumerate(maze):
        for element_index, element in enumerate(row):
            #in my input this was the starting direction, for more inputs there are 3 more conditionals to add.
            if element == "^":
                print("starting position is: ", [row_index, element_index])
                return(row_index, element_index)


def move_up(maze, position, visited_positions):

    visited_positions.add(position)
    print("total visited positions: ", len(visited_positions))
    
    next_position = (position[0] - 1, position[1])

    if next_position[0] == -1:
        print("route is finished, total visited positions: ", len(visited_positions))
        return

    if maze[next_position[0]][next_position[1]] == "#":
        print("there is an obstacle, turning right")
        return move_right(maze, position, visited_positions)

    print("moving up")
    return move_up(maze, next_position, visited_positions)

    
def move_right(maze, position, visited_positions):

    visited_positions.add(position)
    print("total visited positions: ", len(visited_positions))
    
    next_position = (position[0], position[1] + 1)

    if next_position[1] == len(maze):
        print("route is finished, total visited positions: ", len(visited_positions))
        return

    if maze[next_position[0]][next_position[1]] == "#":
        print("there is an obstacle, turning down")
        return move_down(maze, position, visited_positions)

    print("moving right")
    return move_right(maze, next_position, visited_positions)


def move_down(maze, position, visited_positions):

    visited_positions.add(position)
    print("total visited positions: ", len(visited_positions))
    
    next_position = (position[0] + 1, position[1])

    if next_position[0] == len(maze):
        print("route is finished, total visited positions: ", len(visited_positions))
        return

    if maze[next_position[0]][next_position[1]] == "#":
        print("there is an obstacle, turning left")
        return move_left(maze, position, visited_positions)

    print("moving down")
    return move_down(maze, next_position, visited_positions)


def move_left(maze, position, visited_positions):

    visited_positions.add(position)
    print("total visited positions: ", len(visited_positions))
    
    next_position = (position[0], position[1] - 1)

    if next_position[1] == -1:
        print("route is finished, total visited positions: ", len(visited_positions))
        return

    if maze[next_position[0]][next_position[1]] == "#":
        print("there is an obstacle, turning up")
        return move_up(maze, position, visited_positions)

    print("moving left")
    return move_left(maze, next_position, visited_positions)

def solver(maze):
    position = find_starting_position(maze)
    #mark starting position
    visited_positions = set()
    visited_positions.add(position)
    print(visited_positions)
    move_up(maze, position, visited_positions)

with open("6_actual_input.txt", "r") as file:
    maze = [list(line.strip()) for line in file]
    solver(maze)