MIN_X = 0
MIN_Y = 0
MAX_X = 4
MAX_Y = 4

# Number of steps moved in the X and Y axis for each direction
MOVE_STEPS = {
  "east": (1, 0),
  "north": (0, 1),
  "west": (-1, 0),
  "south": (0, -1),
}

WECLOME_MESSAGE = """
Welcome to the Toy Robot program!
Place your robot anywhere on the 5x5 table and starting moving around!

Valid commands (case insensitive):
PLACE <X position>,<Y position>,<facing - NORTH|SOUTH|EAST|WEST>
MOVE - move one step forward
LEFT - turn 90 degrees counter-clockwise
RIGHT - turn 90 degrees clockwise
REPORT - show your current location
"""


class Robot:
  def __init__(self):
    self.x = None
    self.y = None
    self.f = None


  def move(self):
    next_x = self.x + MOVE_STEPS[self.f][0]
    next_y = self.y + MOVE_STEPS[self.f][1]

    if (MIN_X <= next_x <= MAX_X) is False or (MIN_Y <= next_y <= MAX_Y) is False:
      print("Error: Your robot is going to fall off the table if you move!")
      return

    self.x = next_x
    self.y = next_y

    print("Your robot has moved!")


  def place(self, x_pos, y_pos, facing):
    try:
      x_pos = int(x_pos)
    except ValueError:
      print("Error: X coordinate must be an integer!")
      return

    try:
      y_pos = int(y_pos)
    except ValueError:
      print("Error: Y coordinate must be an integer!")
      return

    if (MIN_X <= x_pos <= MAX_X) is False or (MIN_Y <= y_pos <= MAX_Y) is False:
      print("Error: Placing your robot there will fall off the table!")
      return

    if facing not in MOVE_STEPS:
      print("Error: Your robot can only face NORTH/ SOUTH/ EAST/ WEST")
      return

    self.x = x_pos
    self.y = y_pos
    self.f = facing
    print("Your robot has been placed!")


  def report(self):
    print(f"Your robot is at ({self.x}, {self.y}) facing {self.f}")


  def turn(self, is_left: bool):
    directions = list(MOVE_STEPS.keys())

    # Get current facing index
    facing_index = directions.index(self.f) # East is 0, North is 1 etc

    # Get new facing index
    facing_index += 1 if is_left else -1
    facing_index %= 4

    self.f = directions[facing_index]
    print("Your robot has turned!")


  def do_robot_action(self):
    input_command = input("\nYour next move: ")

    is_input_empty = input_command == ""
    if is_input_empty:
      print("You must enter a command for the robot!")
      return

    # Separate the main action from the rest of the arguments
    [action, *args] = input_command.strip().lower().split(" ", 1)

    is_valid_action = action in ["place", "move", "left", "right", "report"]
    if not is_valid_action:
      print(f"Invalid action: {action.upper()}")
      return

    # Split the arguments by comma and remove trailing whitespaces
    args = [arg.strip() for arg in args[0].split(",")] if len(args) else []

    has_placed_robot = self.x is not None
    if has_placed_robot is False and action != "place":
      print("You must PLACE the robot first before doing anything else!")
      return

    if action == "place":
      if len(args) < 3:
        print("Error: 3 arguments needed to place robot: X, Y, facing")
        return

      if len(args) > 3:
        print("Error: Too many arguments, only 3 expected!")
        return
      
      self.place(*args)
      return
    
    if len(args):
      print(f"Error: No arguments required for {action.upper()}!")
      return

    if action == "report":
      self.report()

    elif action == "move":
      self.move()
      return
    
    else:
      is_left = action == "left"
      self.turn(is_left)


print(WECLOME_MESSAGE)
robot = Robot()
while True:
  robot.do_robot_action()
