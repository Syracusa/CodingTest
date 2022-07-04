from collections import *

IS_RELEASE = False
if not IS_RELEASE:
    import sys
    sys.stdin = open("input1.txt", "r")

# Utility Function
## Debug print
def dprt(logstr):
    if IS_RELEASE == False:
        print(logstr)

# Constant
TILT_UP, TILT_RIGHT, TILT_DOWN, TILT_LEFT = [elem for elem in range(4)]
DIR_STR = ['TILT_UP', 'TILT_RIGHT', 'TILT_DOWN', 'TILT_LEFT' ]
# Class
class Board:
    def __init__(self, arr):
        for _ in arr:
            self.arr = [l[:] for l in arr]
        self.size = len(arr)
        self.addable = [[True for _ in range(len(arr))] for __ in range(len(arr))]

    def dprt(self):
        if not IS_RELEASE:
            for i in range(self.size):
                print(self.arr[i])

    def get_maxval(self):
        max = 0
        for xpos in range(self.size):
            for ypos in range(self.size):
                if self.arr[ypos][xpos] > max:
                    max = self.arr[ypos][xpos]
        
        return max

    def is_in_board(self, xpos, ypos):
        if xpos >= 0 and xpos < self.size and \
                ypos >= 0 and ypos < self.size:
            return True
        return False


    def tilt_one(self, xpos, ypos, xdir, ydir):
        if self.arr[ypos][xpos] == 0:
            return
        
        nextx = xpos + xdir
        nexty = ypos + ydir
        if not self.is_in_board(nextx, nexty):
            return

        while self.arr[nexty][nextx] == 0:
            nextx += xdir
            nexty += ydir
            if not self.is_in_board(nexty, nextx):
                prev = self.arr[ypos][xpos]
                self.arr[ypos][xpos] = 0
                self.arr[nexty - ydir][nextx - xdir] = prev
                return

        if self.arr[nexty][nextx] == self.arr[ypos][xpos]:
            if self.addable[nexty][nextx]:
                self.arr[nexty][nextx] *= 2
                self.arr[ypos][xpos] = 0
                self.addable[nexty][nextx] = False
                return

        self.arr[ypos][xpos] = 0
        self.arr[nexty - ydir][nextx - xdir] = self.arr[ypos][xpos]


    def tilt_xydir(self, xdir, ydir):
        if xdir > 0:
            xstart = self.size - 1
            xend = -1
            xstep = -1
        else: 
            xstart = 0
            xend = self.size
            xstep = 1

        if ydir > 0:
            ystart = self.size - 1
            yend = -1
            ystep = -1
        else: 
            ystart = 0
            yend = self.size
            ystep = 1

        for xpos in range(xstart, xend, xstep):
            for ypos in range(ystart, yend, ystep):
                self.tilt_one(xpos, ypos, xdir, ydir)
                dprt(f'{xpos} {ypos}')
        pass

    def tilt(self, dir):
        xdir = 0
        ydir = 0        
        if dir == TILT_UP:
            ydir = -1
        elif dir == TILT_LEFT:
            xdir = -1
        elif dir == TILT_RIGHT:
            xdir = 1
        elif dir == TILT_DOWN:
            ydir = 1
        else:
            dprt('error')

        self.tilt_xydir(xdir, ydir)

        

# Function
def get_input():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    return N, arr

dirs = [TILT_UP, TILT_RIGHT, TILT_DOWN, TILT_LEFT]

def tilt_dfs(board: Board, depth):
    if (depth == 2):
        return board.get_maxval()

    max = 0
    for dir in dirs:
        newboard = Board(board.arr)
        newboard.tilt(dir)
        dprt(f'depth:{depth} tilt:{DIR_STR[dir]}')
        newboard.dprt()
        val = tilt_dfs(newboard, depth + 1)
        if val > max:
            max = val
    
    return max

def solve():
    N, arr = get_input()
    board = Board(arr)
    board.dprt()
    print(tilt_dfs(board, 0))
    
# Main
solve()