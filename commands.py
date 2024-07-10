from robot import Robot
from tabletop import Tabletop

class CommandProcessor:
    def __init__(self):
        self.robot = Robot()
        self.tabletop = Tabletop()

    def process(self, command):
        try:
            if command.startswith("PLACE"):
                parts = command.split()
                if len(parts) != 2:
                    raise ValueError("Invalid PLACE command format.")
                params = parts[1].split(",")
                if len(params) != 3:
                    raise ValueError("Invalid PLACE command parameters.")
                x, y, facing = params
                x, y = int(x), int(y)
                if self.tabletop.is_on_table(x, y):
                    self.robot.place(x, y, facing)
                else:
                    return "Error processing command '{}': PLACE command parameters out of tabletop bounds.".format(command)
            elif command == "MOVE":
                if self.robot.x is None or self.robot.y is None:
                    return "Error processing command '{}': MOVE command cannot be executed before PLACE command.".format(command)
                self.robot.move()
            elif command == "LEFT":
                if self.robot.x is None or self.robot.y is None:
                    return "Error processing command '{}': LEFT command cannot be executed before PLACE command.".format(command)
                self.robot.left()
            elif command == "RIGHT":
                if self.robot.x is None or self.robot.y is None:
                    return "Error processing command '{}': RIGHT command cannot be executed before PLACE command.".format(command)
                self.robot.right()
            elif command == "REPORT":
                if self.robot.x is None or self.robot.y is None:
                    return "Error processing command '{}': REPORT command cannot be executed before PLACE command.".format(command)
                return self.robot.report()
            else:
                return "Error processing command '{}': Invalid command.".format(command)
        except (ValueError, IndexError) as e:
            return "Error processing command '{}': {}".format(command, e)
        return None
