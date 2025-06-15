class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0, 0]
        direction = [0, 1]  # Horizontal 0, Vertical 1

        def changeDir(direction, cmd):
            if cmd == 'L':
                if direction == [0, 1]:
                    return [-1, 0]
                elif direction == [-1, 0]:
                    return [0, -1]
                elif direction == [0, -1]:
                    return [1, 0]
                else:
                    return [0, 1]
            else:
                if direction == [0, 1]:
                    return [1, 0]
                elif direction == [1, 0]:
                    return [0, -1]
                elif direction == [0, -1]:
                    return [-1, 0]
                else:
                    return [0, 1]

        for cmd in instructions:
            if cmd == 'G':
                start[0] += direction[0]
                start[1] += direction[1]
            else:
                direction = changeDir(direction, cmd)

        return not (start != [0, 0] and direction == [0, 1])
