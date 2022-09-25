import logging

logger = logging.getLogger() 

class Board:
    """
    A simple Board Class
    """
    def __init__(self, size):
        self.size = size
        self.max_x = size - 1
        self.max_y = size - 1
        self.obstructions = []

    def _xy_is_valid(self,x,y):
        """
        Checks if provided x,y is valid for the board

        Args:
            x (int): x axis value
            y (int): y axis value

        Returns:
            Bool: True or False
        """
        return_value = True
        if str(x).isdigit() and str(y).isdigit():
            if x > self.max_x or x < 0:
                logger.error("Location is outside the board. The x axis value is invalid.")
                return_value = False
            if y > self.max_y or y < 0:
                logger.error("Location is outside the board. The y axis value is invalid.")
                return_value = False
            return return_value
        else:            
            logger.error("Invalid value for x and/or y. Please pass integer values.")
            return_value = False
            return return_value

    def _xy_is_empty(self,x,y):
        """
        Checks if provided x,y  is empty on the board

        Args:
            x (int): x axis value
            y (int): y axis value

        Returns:
            Bool: True or False
        """
        if [x,y] not in self.obstructions:
            return True
        else:
            logger.error(f"Tile [{x},{y}] is not empty.")
            return False

    def add_obstruction(self,x,y):
        """
        Adds obstruction on the board object

        Args:
            x (int): x axis value
            y (int): y axis value

        Returns:
            Bool: True or False
        """
        if self._xy_is_valid(x,y) and self._xy_is_empty(x,y):
            self.obstructions.append([x,y])
            return True
        else:
            return False

    def remove_obstruction(self,x,y):
        """
        Removes obstruction on the board object

        Args:
            x (int): x axis value
            y (int): y axis value

        Returns:
            Bool: True or False
        """
        if [x,y] in self.obstructions:
            self.obstructions.remove([x,y])
            return True
        else:
            return False

    def get_board_state(self):
        """
        Returns the state of the board in list format. It can be parsed to display the state of the board via print.

        Returns:
            list: list of lists containing data state of the board
        """
        board_state = [[0 for count in range(int(self.size))] for count in range(int(self.size))]
        for obj in self.obstructions:
            x_axis = obj[0]
            y_axis = self.max_y - obj[1]
            board_state[y_axis][x_axis] = 1
        return board_state