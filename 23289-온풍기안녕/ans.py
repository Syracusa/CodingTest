import sys

DEBUG = True

if DEBUG:
    sys.stdin = open("input1.txt", "r")

def dprt(dlog):
    if DEBUG:
        print(dlog)

class Room:
    def init(self, arr, warr):
        self.arr = list(l[:] for l in arr)
        self.walls = list(l[:] for l in warr)
        self.ysize = len(arr[0])
        self.xsize = len(arr)
        self.wallnum = len(warr)
        return self

    def dprt(self):
        if DEBUG:
            for row in range(self.height):
                print(self.arr[row])
    
    def dprt_wall(self):
        if DEBUG:
            for wn in range(self.wallnum):
                print(self.walls[wn])
        
        pass    

def get_input():
    R, C, K = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    
    W = (int)(sys.stdin.readline())
    range(W)
    warr = [list(map(int, sys.stdin.readline().split())) for _ in range(W)]

    return arr, warr

def solve():
    arr, warr = get_input()
    room = Room().init(arr, warr)
    room.dprt()
    room.dprt_wall()

solve()
