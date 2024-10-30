# Mars Rover Simulation

This project is a simulation of a Mars Rover's movement across a defined grid. The program accepts user input to configure the grid dimensions, the rover's initial position and orientation, and a set of movement commands. The simulation outputs the rover's final position and orientation after executing the commands, and marks the rover as "LOST" if it attempts to move out of grid bounds.

## Code Overview
The program is organized into several functions:

**turn**: Calculates the new direction of the rover when a turn command (L or R) is issued.

**move_forward**: Moves the rover forward based on its current direction.

**simulate_robot**: Simulates the rover's movement according to the command sequence and detects if the rover goes out of bounds.

**parse_initial_state**: Parses the initial state input string, extracting x, y, and direction.

**main**: Main loop for taking input and outputting results.


## Features

- **Grid Definition**: Configurable grid size that restricts rover movement within its boundaries.
- **Command Set**: Supports three commands:
  - `L` - Turn left
  - `R` - Turn right
  - `F` - Move forward
- **Out-of-Bounds Detection**: Flags the rover as "LOST" if it moves outside the grid.

## Error Handling

**Invalid Commands**: An error message is displayed if any command other than L, R, or F is used.

**Invalid Grid or Position**: The program checks for valid grid dimensions and position format, handling errors gracefully.



### Prerequisites
This program requires Python 3.x to run.

### Running the Simulation

1. Clone the Git Repository:

     ```git clone https://github.com/sandeepreddyvennam/mars_rover_project.git```

     ```cd mars_rover_project```

2. Execute the script from the terminal:
   
    ``` python mars_rover_simulation.py ```

3. Follow the prompts to input the grid size, initial rover position, and commands.


## Input Format
**Grid Size:** Enter the grid dimensions as width and height separated by a space (e.g., 4 8).

**Rover Position and Commands:** Enter the initial state of the rover in the format (x, y, D) COMMANDS, 
**where:**

- `x`, `y`: Initial coordinates of the rover

- `D`: Initial direction, one of N (North), E (East), S (South), or W (West)

- `COMMANDS`: Sequence of commands, using L, R, and F.

Example: (2,3,E) LFRFF

**Sample Run**
```
Enter grid size (e.g., '4 8'): 4 8
Enter robot position and commands (e.g., '(2,3,E) LFRFF'): (2,3,E) LFRFF
(4, 4, E)
Enter robot position and commands (e.g., '(2,3,E) LFRFF'): (0,0,S) FFF
(0, 0, S) LOST
```
To exit the simulation, simply press Enter on an empty line when prompted for the robot position and commands.


## Future Enhancements
- Add support for multiple rovers.
- Implement obstacle detection within the grid.
- Save movement history for each rover.