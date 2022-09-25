import logging

from board import Board
from robot import Robot

logger = logging.getLogger() 

def run_command(command, board, robot):
    """
    Runs a command provided a robot and board class object

    Args:
        command (str): command to run
        board (Board): Board object
        robot (Robot): Robot object

    Returns:
        Bool: True / False / 'Exit'
    """
    command = command.upper()
    if command == 'EXIT':
        return 'EXIT'
    elif 'PLACE' in command:
        try:
            place_commands = command.replace(' ','').replace('PLACE','').split(',')
            x = place_commands[0]
            y = place_commands[1]
            f = place_commands[2]
            return robot.place(x, y, f, board)
        except Exception as e:
            # logger.error(f"Exception: {e}")
            logger.error("Invalid PLACE command. Please use the following command pattern: 'PLACE x,y,f'")
            return False
    elif robot.board is None:
        logger.warning("Robot not yet placed on the board. Ignoring command.")
        return False
    elif command in ('LEFT','RIGHT'):
        robot.rotate(command)
    elif command == 'MOVE':
        robot.move()
    elif command == 'REPORT':
        return robot.report()
    else:
        logger.error("Invalid command. Please try again.")
        return False

if __name__ == "__main__":    
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    print('#################################################################')
    print("#              Welcome to the toy robot simulator!              #")
    print('#################################################################\n')
    print('--------------------- Initializing objects! ---------------------')
    print("Creating board of size 5x5")
    b1 = Board(5)
    print("Creating 1 robot")
    r1 = Robot()
    print('-----------------------------------------------------------------')
    print("""
        ----------------------- Command list ----------------------------
        > PLACE x,y,f
            - Places the robot on the board
            - Repositions if the robot already on the board
            - Parameters:
               x = x-axis where to place the robot
               y = y-axis where to place the robot
               f = robot facing orientation (NORTH, EAST, WEST, SOUTH)
        > MOVE
            - Move one tile where robot is facing
        > LEFT
            - Rotate robot to the left
        > RIGHT
            - Rotate robot to the right
        > REPORT
            - Print current state of robot in x,y,f format
        > EXIT
            - Exit application        
        -----------------------------------------------------------------
        """.replace('        ',''))
    robot_command = None
    while robot_command != 'EXIT':
        print("-----------------------------------------------------------------")
        inp = input("Please enter command: ")
        robot_command = run_command(inp, b1, r1)
