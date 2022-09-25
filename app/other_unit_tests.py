import logging
import unittest

from start_app import run_command
from board import Board
from robot import Robot


logging.basicConfig(level=logging.CRITICAL)

board_size = 5

class TestIOHandling(unittest.TestCase):
    
    # The application should discard all commands in the sequence until a valid PLACE command has been executed
    # A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands
    def test_valid_input_before_place(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('MOVE', b1, r1)
        self.assertIsNone(r1.board)
    
    # Try invalid input after place. Should ignore invalid input and robot should be on same state
    def test_invalid_input_after_place(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('this_is_an_invalid_command', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,NORTH')

    # Try to pass invalid x,y value on PLACE command. Should ignore.
    def test_invalid_place_xy_input(self):
        b1 = Board(board_size)
        r1 = Robot()
        result = run_command('PLACE x,y,NORTH', b1, r1)
        self.assertFalse(result)
    
    # Try to pass invalid f value on PLACE command. Should ignore.
    def test_invalid_place_f_input(self):
        b1 = Board(board_size)
        r1 = Robot()
        result = run_command('PLACE 0,0,TEST', b1, r1)
        self.assertFalse(result)

    # Try to issue valid place command but it has extra spaces on random location
    def test_valid_place_with_extra_spaces(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('  PLACE     0 , 0 , NORTH   ', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,NORTH')

    # The application should discard all commands in the sequence until a valid PLACE command has been executed.
    def test_invalid_first_command_valid_succeeding_commands(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('this_is_an_invalid_command', b1, r1)
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,1,NORTH')

    # The application should be able to handle lower case commands
    def test_lower_case_input(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('place 0,0,north', b1, r1)
        run_command('move', b1, r1)
        result = run_command('report', b1, r1)
        self.assertEqual(result,'0,1,NORTH')

    # The application should be able to handle mixed case commands
    def test_mixed_case_input(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('Place 0,0,north', b1, r1)
        run_command('Move', b1, r1)
        result = run_command('Report', b1, r1)
        self.assertEqual(result,'0,1,NORTH')

class TestDomainStructureLogic(unittest.TestCase):
    # PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
    def test_valid_place(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,NORTH')

    # MOVE will move the toy robot one unit forward in the direction it is currently facing.
    def test_move_north(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,1,NORTH')

    # MOVE will move the toy robot one unit forward in the direction it is currently facing.
    def test_move_south(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 4,4,SOUTH', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'4,3,SOUTH')

    # MOVE will move the toy robot one unit forward in the direction it is currently facing.
    def test_move_east(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,EAST', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'1,0,EAST')

    # MOVE will move the toy robot one unit forward in the direction it is currently facing.
    def test_move_west(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 4,4,WEST', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'3,4,WEST')
    
    # LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
    def test_rotate_left(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('LEFT', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,WEST')

    # LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
    def test_rotate_right(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('RIGHT', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,EAST')

    # LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
    def test_rotate_left_360(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('LEFT', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,NORTH')
    
    # LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
    def test_rotate_right_360(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('RIGHT', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,NORTH')

    # It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command.
    def test_place_then_commands_then_place(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('PLACE 4,4,NORTH', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'4,4,NORTH')

    # Must be prevented from falling to destruction.
    def test_invalid_x_move(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,WEST', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,WEST')

    # Must be prevented from falling to destruction.
    def test_invalid_y_move(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,SOUTH', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,SOUTH')

    # Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.
    def test_invalid_xy_move_then_more_valid_moves(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,SOUTH', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'2,0,EAST')

    # Cannot place outside the board
    def test_invalid_place_x(self):
        b1 = Board(board_size)
        r1 = Robot()
        result = run_command('PLACE 999,0,NORTH', b1, r1)
        self.assertEqual(result,False)

    # Cannot place outside the board
    def test_invalid_place_y(self):
        b1 = Board(board_size)
        r1 = Robot()
        result = run_command('PLACE 0,999,NORTH', b1, r1)
        self.assertEqual(result,False)

    # Test 2 place commands, assuming that the 2nd place command would reset the activity
    def test_two_place_commands(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('PLACE 4,4,NORTH', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'4,4,NORTH')

    # Test 2 place on the same xy but different orientation. Should update the robot facing orientation.
    def test_two_place_commands_same_xy(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('PLACE 0,0,SOUTH', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,SOUTH')

class TestExamples(unittest.TestCase):
    # Input sample 1 from test
    def test_example_1(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,1,NORTH')

    # Input sample 2 from test
    def test_example_2(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,NORTH', b1, r1)
        run_command('LEFT', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'0,0,WEST')

    # Input sample 3 from test
    def test_example_3(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 1,2,EAST', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'3,3,NORTH')

    # Attempt to go lower right of board
    def test_example_4(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,EAST', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'4,0,EAST')

    # Attempt to go upper right of with attempts to go off the board
    def test_example_5(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,0,EAST', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1) # off board move, should ignore
        run_command('LEFT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'4,4,NORTH')

    # Attempt to go from upper left of board to lower right of board via middle
    def test_example_5(self):
        b1 = Board(board_size)
        r1 = Robot()
        run_command('PLACE 0,4,EAST', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('LEFT', b1, r1)
        run_command('MOVE', b1, r1)
        run_command('RIGHT', b1, r1)
        run_command('MOVE', b1, r1)
        result = run_command('REPORT', b1, r1)
        self.assertEqual(result,'4,0,SOUTH')

if __name__ == "__main__":
    unittest.main(verbosity=2)