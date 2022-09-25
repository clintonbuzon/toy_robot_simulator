# Toy Robot Simulator

## What is it?

This is a toy robot simulator made using python. The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed. The origin (0,0) can be considered to be the SOUTH WEST most corner.

## Command list

- `PLACE x,y,f`
	- Places the robot on the board
	- Repositions if the robot is already on the board
	- Parameters:
		- x = x-axis where to place the robot
		- y = y-axis where to place the robot
		- f = robot facing orientation (NORTH, EAST, WEST, SOUTH)
	- Example: `PLACE 0,0,NORTH` will place the robot on the lower left most side of the board facing north
- `MOVE`
	- Move one tile where the robot is facing
- `LEFT`
	- Rotate the robot 90 degrees to the left
- `Right`
	- Rotate the robot 90 degrees to the right
- `REPORT`
	- Print current state of robot in x,y,f format
	- Will also print current state of the board where `0` is empty while `1` is the current location of the robot
- `EXIT`
	- Exit the application

It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. Running another PLACE command while the robot is already on the board will relocate the current robot to the new location and new facing orientation. The application should discard all commands in the sequence until a valid PLACE command has been executed.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Exam Unit Tests](#exam-unit-tests)
	- [Test Output](#test-output)
- [Other Unit Tests](#other-unit-tests)
	- [Test Output](#test-output-1)
- [Extensibility](#extensibility)
- [License](#license)

## Install

This project was built using python 3.7 but has been tox tested to be working on 3.6 and 3.8. Default python libraries were used thus, no need to install additional libraries.

## Usage

Clone this repository on to your local machine with Python version 3.6/3.7/3.8 and call the `start_app.py` file

```Python
cd <local_clone_path>
cd app
python3 start_app.py
```

## Exam Unit Tests

To run the exam unit tests, you may trigger the `exam_unit_tests.py` or issue the `python3 -m unittest exam_unit_tests.py` command.

```Python
cd <local_clone_path>
cd app
python3 exam_unit_tests.py
# or
python3 -m unittest -v exam_unit_tests.py
```
#### Test Output

```bash
test_example_1 (exam_unit_tests.TestExamScenarios) ... 
INFO: Robot added to board successfully.
INFO: Successfully moved from [0,0] to [0,1].
INFO: Robot State = 0,1,NORTH
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [1, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
ok
test_example_2 (exam_unit_tests.TestExamScenarios) ... 
INFO: Robot added to board successfully.
INFO: Successfully rotated from NORTH to WEST.
INFO: Robot State = 0,0,WEST
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [1, 0, 0, 0, 0]
ok
test_example_3 (exam_unit_tests.TestExamScenarios) ... 
INFO: Robot added to board successfully.
INFO: Successfully moved from [1,2] to [2,2].
INFO: Successfully moved from [2,2] to [3,2].
INFO: Successfully rotated from EAST to NORTH.
INFO: Successfully moved from [3,2] to [3,3].
INFO: Robot State = 3,3,NORTH
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 1, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
INFO: [0, 0, 0, 0, 0]
ok

----------------------------------------------------------------------
Ran 3 tests in 0.034s

OK
```
## Other Unit Tests

To run the other unit tests, you may trigger the `other_unit_tests.py` or issue the `python3 -m unittest other_unit_tests.py` command.

```Python
cd <local_clone_path>
cd app
python3 other_unit_tests.py
# or
python3 -m unittest -v other_unit_tests.py
```
#### Test Output

```bash
test_invalid_place_x (__main__.TestDomainStructureLogic) ... ok
test_invalid_place_y (__main__.TestDomainStructureLogic) ... ok
test_invalid_x_move (__main__.TestDomainStructureLogic) ... ok
test_invalid_xy_move_then_more_valid_moves (__main__.TestDomainStructureLogic) ... ok
test_invalid_y_move (__main__.TestDomainStructureLogic) ... ok
test_move_east (__main__.TestDomainStructureLogic) ... ok
test_move_north (__main__.TestDomainStructureLogic) ... ok
test_move_south (__main__.TestDomainStructureLogic) ... ok
test_move_west (__main__.TestDomainStructureLogic) ... ok
test_place_then_commands_then_place (__main__.TestDomainStructureLogic) ... ok
test_rotate_left (__main__.TestDomainStructureLogic) ... ok
test_rotate_left_360 (__main__.TestDomainStructureLogic) ... ok
test_rotate_right (__main__.TestDomainStructureLogic) ... ok
test_rotate_right_360 (__main__.TestDomainStructureLogic) ... ok
test_two_place_commands (__main__.TestDomainStructureLogic) ... ok
test_two_place_commands_same_xy (__main__.TestDomainStructureLogic) ... ok
test_valid_place (__main__.TestDomainStructureLogic) ... ok
test_example_1 (__main__.TestExamples) ... ok
test_example_2 (__main__.TestExamples) ... ok
test_example_3 (__main__.TestExamples) ... ok
test_example_4 (__main__.TestExamples) ... ok
test_example_5 (__main__.TestExamples) ... ok
test_invalid_first_command_valid_succeeding_commands (__main__.TestIOHandling) ... ok
test_invalid_input_after_place (__main__.TestIOHandling) ... ok
test_invalid_place_f_input (__main__.TestIOHandling) ... ok
test_invalid_place_xy_input (__main__.TestIOHandling) ... ok
test_lower_case_input (__main__.TestIOHandling) ... ok
test_mixed_case_input (__main__.TestIOHandling) ... ok
test_valid_input_before_place (__main__.TestIOHandling) ... ok
test_valid_place_with_extra_spaces (__main__.TestIOHandling) ... ok

----------------------------------------------------------------------
Ran 30 tests in 0.036s

OK
```

## Extensibility

Current code was made with extensibility in mind without adding too much complexity. We can quickly modify the code to add more features easily like:

- Make the table size configurable
- Add 2 (or n) robots on the table
- Add more directions
- Add obstacles/obstructions
- etc.

[GNU](LICENSE) © John Clinton Buzon