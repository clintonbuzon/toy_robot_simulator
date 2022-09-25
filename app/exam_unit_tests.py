import logging
import unittest

from start_app import run_command
from board import Board
from robot import Robot


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

board_size = 5

class TestExamScenarios(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main(verbosity=2)