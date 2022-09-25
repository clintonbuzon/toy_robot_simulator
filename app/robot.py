import logging

logger = logging.getLogger() 

class Robot:
    """
    A simple Robot Class
    """
    def __init__(self):
        self.x_axis = None
        self.y_axis = None
        self.facing = None
        self.board = None

    def _is_valid_facing(self, f):
        """
        Checks if facing value is valid. Will capture latest list of facing values from generate_moveset()

        Args:
            f (str): Facing string value

        Returns:
            Bool: True or False
        """
        moveset = self.generate_moveset()
        if next((x for x in moveset if x["facing"] == f), False):
            return True
        else:
            logger.error("Invalid facing value.")
            return False
    
    def _is_digit_xy(self, x, y):
        """
        Checks if provided x axis and y axis values are both integers

        Args:
            x (_type_): x axis
            y (_type_): y axis

        Returns:
            Bool: True or False
        """
        if str(x).isdigit() and str(y).isdigit():
            return True
        else:
            logger.error("Invalid value for x and/or y. Please pass integer values.")
            return False

    def generate_moveset(self):
        """
        Generate all possible moves based on current Robot's state.
        Update moveset variable to add more moves like NORTHWEST, SOUTHEAST, etc.

        Returns:
            list: list of dictionaries. Each dictionary will contain all valid moveset
        """
        x_axis = self.x_axis
        y_axis = self.y_axis
        
        if self.x_axis is None and self.y_axis is None: # if robot not on board yet, generate position on defualt location of 0,0
            x_axis = 0
            y_axis = 0

        # can easily add more moves if needed like diagonal moves NORTHWEST, SOUTHEAST, etc.
        moveset = [
            {"facing": "NORTH",     "LEFT": "WEST",     "RIGHT": "EAST",     "MOVE": f"[{x_axis},{y_axis+1}]"},
            {"facing": "EAST",      "LEFT": "NORTH",    "RIGHT": "SOUTH",    "MOVE": f"[{x_axis+1},{y_axis}]"},
            {"facing": "WEST",      "LEFT": "SOUTH",    "RIGHT": "NORTH",    "MOVE": f"[{x_axis-1},{y_axis}]"},
            {"facing": "SOUTH",     "LEFT": "EAST",     "RIGHT": "WEST",     "MOVE": f"[{x_axis},{y_axis-1}]"},
        ]
        return moveset

    def place(self, x, y, f, board):
        """
        Place a robot on a board object. 

        Args:
            x (int): x axis value
            y (int): y axis value
            f (str): facing orientation
            board (Board): Class Board object

        Returns:
            Bool: True or False if valid place was done or not
        """
        if self._is_digit_xy(x,y) and self._is_valid_facing(f):
            x_int = int(x)
            y_int = int(y)
            if self.board is not None: # if robot is already in the board
                logger.info("Attempting to reposition the robot.")

                if self.x_axis == x_int and self.y_axis == y_int: # if repositioning on same location, allow change in facing direction
                    self.facing = f
                elif self.move(x_int, y_int):
                    self.facing = f
                else:
                    return False

                logger.info("Repositioning robot success.")
                return True
            elif board.add_obstruction(x_int, y_int):
                logger.info("Robot added to board successfully.")
                self.board = board
                self.x_axis = x_int
                self.y_axis = y_int
                self.facing = f
                return True
            else:
                return False
        else:
            return False

    def report(self):
        """
        Output current state or the robot

        Returns:
            str: String state of robot in x,y,f format
        """
        report_string = f"{self.x_axis},{self.y_axis},{self.facing}"
        logger.info(f"Robot State = {report_string}")
        for row in self.board.get_board_state():
            logger.info(row)
        return report_string

    def rotate(self, direction):
        """
        Updates the facing orientation value of the robot depending on the rotate parameter

        Args:
            direction (str): LEFT or RIGHT
        """
        moveset = self.generate_moveset()
        old_facing = self.facing
        new_facing = next(x for x in moveset if x["facing"] == self.facing)[direction]
        self.facing = new_facing
        logger.info(f"Successfully rotated from {old_facing} to {new_facing}.")

    def move(self, x=None, y=None):
        """
        Updates the x and y of the robot. By default it moves one tile forward based on current state of robot.
        If x and y values are passed, then it can move directly to the provided x,y value

        Args:
            x (int, optional): x axis value. Defaults to None.
            y (int, optional): y axis value. Defaults to None.

        Returns:
            Bool: True or False
        """
        moveset = self.generate_moveset()
        old_x_axis = self.x_axis
        old_y_axis = self.y_axis
        
        if x is not None and y is not None: # if x and y was provided
            new_x_axis = x
            new_y_axis = y
        else: # regular move command to move 1 tile where it's facing
            move_location = eval(next(x for x in moveset if x["facing"] == self.facing)["MOVE"])
            new_x_axis = move_location[0]
            new_y_axis = move_location[1]

        if self.board.add_obstruction(new_x_axis,new_y_axis):
            self.board.remove_obstruction(old_x_axis,old_y_axis)
            self.x_axis = new_x_axis
            self.y_axis = new_y_axis
            logger.info(f"Successfully moved from [{old_x_axis},{old_y_axis}] to [{new_x_axis},{new_y_axis}].")
            return True
        
        
      
