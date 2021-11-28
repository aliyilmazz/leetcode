from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Robot:

    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.direction = Direction.NORTH.value

    def move(self):
        if self.direction == Direction.NORTH.value:
            self.y_position += 1
        elif self.direction == Direction.EAST.value:
            self.x_position += 1
        elif self.direction == Direction.SOUTH.value:
            self.y_position -= 1
        elif self.direction == Direction.WEST.value:
            self.x_position -= 1

    def steer_left(self):
        self.direction = (self.direction + 1) % 4

    def steer_right(self):
        self.direction = (self.direction - 1) % 4


class Solution:

    def __init__(self):
        self.robot = Robot()

    def _process_instructions(self, instructions):
        for instruction in instructions:
            if instruction == 'G':
                self.robot.move()
            elif instruction == 'L':
                self.robot.steer_left()
            elif instruction == 'R':
                self.robot.steer_right()

    def isRobotBounded(self, instructions: str) -> bool:
        self._process_instructions(instructions)
        print("### robot coords: %s %s" % (self.robot.x_position, self.robot.y_position))

        if self.robot.x_position == 0 and self.robot.y_position == 0:
            # robot does not move
            return True

        else:
            # robot moves...

            if self.robot.direction != Direction.NORTH.value:
                #... in a different direction
                return True

        return False


if __name__ == '__main__':
    instructions = "GGLLGG"
    output = Solution().isRobotBounded(instructions)
    print("Instructions:%s\nOutput:%s" % (instructions, output))

    instructions = "GG"
    output = Solution().isRobotBounded(instructions)
    print("Instructions:%s\nOutput:%s" % (instructions, output))

    instructions = "GL"
    output = Solution().isRobotBounded(instructions)
    print("Instructions:%s\nOutput:%s" % (instructions, output))