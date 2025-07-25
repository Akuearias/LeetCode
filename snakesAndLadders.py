'''

LeetCode Exercise #909. Snakes and Ladders

You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.



Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1


Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n^2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.

'''
from typing import List
import collections


# Key words: BFS, matrix, array
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        row = n - 1
        column = 0

        squares = [0] * (n * n + 1)
        dummy = True  # Flag for moving to the right
        for i in range(1, n * n + 1):
            if board[row][column] != -1:
                squares[i] = board[row][column]
            else:
                squares[i] = i
            if dummy is True:
                if column < n - 1:
                    column += 1
                else:
                    row -= 1
                    dummy = False
            else:
                if column > 0:
                    column -= 1
                else:
                    row -= 1
                    dummy = True

        S = 0
        head = 1

        # BFS
        visited = set()
        queue = collections.deque()
        queue.append(head)
        visited.add(head)

        end = n * n

        while queue:
            size = len(queue)
            for _ in range(size): # Track the current case of rolling the die
                curr = queue.popleft()
                for i in range(1, 7):
                    next_sq = curr + i
                    if next_sq <= end:
                        destination = squares[next_sq]
                        if destination not in visited:
                            if destination == end:
                                return S + 1
                            queue.append(destination)
                            visited.add(destination)

            S += 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.snakesAndLadders(board =
                                     [[-1,-1,-1,-1,-1,-1],
                                      [-1,-1,-1,-1,-1,-1],
                                      [-1,-1,-1,-1,-1,-1],
                                      [-1,35,-1,-1,13,-1],
                                      [-1,-1,-1,-1,-1,-1],
                                      [-1,15,-1,-1,-1,-1]]) == 4


