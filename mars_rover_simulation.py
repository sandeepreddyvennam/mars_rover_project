#!/usr/bin/env python
# coding: utf-8

# Constants for directions and movement adjustments
DIRECTIONS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
LEFT_TURN = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RIGHT_TURN = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

def turn(direction, command):
    """Turns the robot left or right based on the command."""
    return LEFT_TURN[direction] if command == 'L' else RIGHT_TURN[direction]

def move_forward(x, y, direction):
    """Moves the robot one step forward in the current direction."""
    dx, dy = DIRECTIONS[direction]
    return x + dx, y + dy

def simulate_robot(x, y, direction, commands, grid_width, grid_height):
    """
    Simulates the robot's movement on the grid according to the command sequence.
    If the robot moves out of the grid bounds, it is marked as LOST.
    """
    for command in commands:
        if command in 'LR':
            direction = turn(direction, command)
        elif command == 'F':
            next_x, next_y = move_forward(x, y, direction)
            if 0 <= next_x <= grid_width and 0 <= next_y <= grid_height:
                x, y = next_x, next_y
            else:
                return x, y, direction, "LOST"
        else:
            raise ValueError(f"Invalid command '{command}'. Use 'L', 'R', or 'F'.")
    return x, y, direction, None

def parse_initial_state(state):
    """
    Parses the initial state of the robot from input, handling spaces and parentheses.
    Returns x, y coordinates and direction.
    """
    parts = state.strip('(').split(',')
    if len(parts) != 3:
        raise ValueError("Invalid initial state format. Expected format: '(x, y, D)'")

    x, y, direction = int(parts[0]), int(parts[1]), parts[2]
    if direction not in DIRECTIONS:
        raise ValueError("Direction must be 'N', 'E', 'S', or 'W'.")
    return x, y, direction

def main():
    """Main function to execute the Mars Rover simulation with input validation."""
    try:
        grid_width, grid_height = map(int, input("Enter grid size (e.g., '4 8'): ").strip().split())
        if grid_width < 0 or grid_height < 0 or (grid_width == 0 and grid_height == 0):
            raise ValueError("Grid dimensions must be non-negative integers.")
    except ValueError as e:
        print(f"Error: Invalid grid size. {e}")
        return

    while True:
        robot_input = input("Enter robot position and commands (e.g., '(2,3,E) LFRFF'): ").strip()
        if not robot_input:
            print("Empty input, exiting the program")
            break  # End input if the line is empty

        try:
            robot_info, commands = robot_input.replace(" ", "").split(')')
            x, y, direction = parse_initial_state(robot_info)
            
            # Simulate robot movement and output final position
            final_x, final_y, final_direction, lost = simulate_robot(
                x, y, direction, commands, grid_width, grid_height
            )
            if lost:
                print(f"({final_x}, {final_y}, {final_direction}) LOST")
            else:
                print(f"({final_x}, {final_y}, {final_direction})")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
