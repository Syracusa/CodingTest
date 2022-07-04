from collections import deque
import copy

IS_RELEASE = True

if IS_RELEASE == False:
    import sys
    sys.stdin = open("input.txt", "r")

# Constant
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

FORWARD_LEANED = 1
NOT_LEANED = 0
BACKWARD_LEANED = -1

# Class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def copyfrom(self, p):
        self.x = p.x
        self.y = p.y

class Board:
    def __init__(self, arr):
        self.row = len(arr)
        self.col = len(arr[0])
        self.arr = arr

    def print(self):
        if IS_RELEASE == False:
            for i in range(self.row):
                for j in range(self.col):
                    print(self.arr[i][j], end='')
                print()

    def get_pos(self, target):
        for i in range(self.row):
            for j in range(self.col):
                if self.arr[i][j] == target:
                    prt('Position of {}: {}-{}'.format(target, i, j))
                    return Point(i, j)
        prt('board has no {}'.format(target))
    
    def get_char(self, pos: Point):
        return self.arr[pos.x][pos.y]
    
    def set_char(self, pos: Point, char):
        self.arr[pos.x][pos.y] = char

    def copyfrom(self, b):
        self.arr = copy.deepcopy(b.arr)
        self.row = len(self.arr)
        self.col = len(self.arr[0])
        
class BoardState:
    def __init__(self):
        self.rpos = Point(0, 0)
        self.bpos = Point(0, 0)
        self.movenum = 0

    def copyfrom(self, boardstate):
        self.movenum = boardstate.movenum
        self.rpos.x = boardstate.rpos.x
        self.rpos.y = boardstate.rpos.y
        self.bpos.x = boardstate.bpos.x
        self.bpos.y = boardstate.bpos.y
        

# Functions
def prt(logstr):
    if IS_RELEASE == False:
        print(logstr)

BALL_IN = 1
BALL_STUCKED = 2
def move_ball(board: Board, target, xdir, ydir):
    ballpos = board.get_pos(target)   
    privpos = Point(ballpos.x, ballpos.y)

    nextpos = Point(ballpos.x + xdir, ballpos.y + ydir)
    nextpos_char = board.get_char(nextpos)
    
    while True:
        if nextpos_char == 'O':
            board.set_char(ballpos, '.')
            return BALL_IN
        elif nextpos_char == '.':
            pass # CONT
        else:
            board.set_char(ballpos, '.')
            board.set_char(privpos, target)
            return BALL_STUCKED
        privpos = Point(nextpos.x, nextpos.y)
        nextpos = Point(nextpos.x + xdir, nextpos.y + ydir)
        nextpos_char = board.get_char(nextpos)

def lean_board_xydir(board: Board, xdir, ydir):
    rpos = board.get_pos('R')
    bpos = board.get_pos('B')

    move_r_first = None

    if ydir == NOT_LEANED:
        if xdir == FORWARD_LEANED:
            if rpos.x > bpos.x:
                move_r_first = True
            else: 
                move_r_first = False
        elif xdir == BACKWARD_LEANED:
            if rpos.x < bpos.x:
                move_r_first = True
            else: 
                move_r_first = False
            pass
        else: 
            prt('error - both not leaned')

    if (xdir == NOT_LEANED):
        if ydir == FORWARD_LEANED:
            if rpos.y > bpos.y:
                move_r_first = True
            else: 
                move_r_first = False
        elif ydir == BACKWARD_LEANED:
            if rpos.y < bpos.y:
                move_r_first = True
            else: 
                move_r_first = False
        else: 
            prt('error - both not leaned')

    if move_r_first == True:
        rres = move_ball(board, 'R', xdir, ydir)
        bres = move_ball(board, 'B', xdir, ydir)
    elif move_r_first == False:
        bres = move_ball(board, 'B', xdir, ydir)
        rres = move_ball(board, 'R', xdir, ydir)
    else:
        prt('error - No move')
    
    return rres, bres

def lean_board_dir(board: Board, dir):
    xdir = None
    ydir = None
    if dir == DIR_UP:
        xdir = NOT_LEANED
        ydir = BACKWARD_LEANED
        pass
    elif dir == DIR_RIGHT:
        xdir = FORWARD_LEANED
        ydir = NOT_LEANED
        pass
    elif dir == DIR_DOWN:
        xdir = NOT_LEANED
        ydir = FORWARD_LEANED
        pass
    elif dir == DIR_LEFT:
        xdir = BACKWARD_LEANED
        ydir = NOT_LEANED
        pass
    else :
        prt("Unavailable direction :", dir)
        return
    
    return lean_board_xydir(board, xdir, ydir)

def find_char(target: str, board: Board):
    for i in range(board.row):
        for j in range(board.col):
            if board.arr[i][j] == target:
                prt('Position of {}: {}-{}'.format(target, i, j))
                return i, j
    return -1, -1

def get_input():
    N,M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    board = Board(arr)
    rpos = board.get_pos('R')
    bpos = board.get_pos('B')

    board.set_char(rpos, '.')
    board.set_char(bpos, '.')

    return Board(arr), rpos, bpos

VISITED = 0
NOT_VISITED = 1
def visit(hmap, rx, ry, bx, by):
    state = (rx, ry, bx, by)
    
    if state in hmap:
        return VISITED
    else:
        hmap[(rx, ry, bx, by)] = VISITED
        return NOT_VISITED

def solve():
    board, rpos, bpos = get_input()
    board.print()

    first_board_state = BoardState()
    first_board_state.rpos = rpos
    first_board_state.bpos = bpos

    boardq = deque([first_board_state])
    dirs = [DIR_DOWN, DIR_UP, DIR_LEFT, DIR_RIGHT]

    vmap = {}

    while True:
        if not boardq:
            print('-1')
            return
            
        board_state = boardq.popleft()
        if (visit(vmap, board_state.rpos.x, board_state.rpos.y, board_state.bpos.x, board_state.bpos.y) == VISITED):
            continue

        for dir in dirs:
            newboardstate = BoardState()
            newboardstate.copyfrom(board_state)
            newboardstate.movenum += 1

            if (newboardstate.movenum > 10):
                print('-1')
                return

            newboard = Board([[]])
            newboard.copyfrom(board)
            newboard.set_char(newboardstate.rpos, 'R')
            newboard.set_char(newboardstate.bpos, 'B')

            prt('board state {}'.format(newboardstate.movenum))
            newboard.print()

            rres, bres = lean_board_dir(newboard, dir)
            if rres == BALL_IN and bres == BALL_STUCKED:
                print(newboardstate.movenum)
                return
            elif rres == BALL_STUCKED and bres == BALL_STUCKED:
                # continue search
                prt('cont')
                newboardstate.rpos = newboard.get_pos('R')
                newboardstate.bpos = newboard.get_pos('B')
                boardq.append(newboardstate)
                pass
            else :
                prt('fail')
                # failed case
                pass

# Main
solve()


# bx, by = find_char('B', board)
# rx, ry = find_char('R', board)

# board.bpos = Point(bx, by)
# board.rpos = Point(rx, ry)

