# Use 2 priority queue
# Max Heap & Min Heap

import sys
from queue import PriorityQueue
import heapq

class ReversePrioirityQueue:
    def __init__(self):
        self.q = PriorityQueue()
        
    def put(self, num):
        self.q.put(num * -1)
        pass

    def get(self):
        res = self.q.get()
        return res * -1

    def qsize(self):
        return self.q.qsize()

def prt_q(q):
    size = q.qsize()
    tempbuf = []
    for _ in range(size):
        tempbuf.append(q.get())
    print(tempbuf)
    for i in range(size):
        q.put(tempbuf[i])

def slow_solve():
    # Min Heap
    q = PriorityQueue()

    # Max Heap
    rq = ReversePrioirityQueue()
    
    number_num = int(sys.stdin.readline())
    
    for i in range(number_num):
        num = int(sys.stdin.readline())
        if i % 2 == 0:
            rq.put(num)
        else:
            q.put(num)
        
        rqe = rq.get()
        print(rqe)
        
        if q.qsize() != 0:
            qe = q.get()
            if rqe > qe:
                q.put(rqe)
                rq.put(qe)
            else:
                q.put(qe)
                rq.put(rqe)
        else:
            rq.put(rqe)
            

if __name__ == "__main__":
    # Priority queue is slow. use heapq
    # slow_solve() 
        
    lq = []
    rq = []
    
    number_num = int(sys.stdin.readline())
    
    for i in range(number_num):
        num = int(sys.stdin.readline())
        if i % 2 == 0:
            heapq.heappush(lq, num * -1)
        else:
            heapq.heappush(rq, num)
            
        lqe = lq[0] * -1
        if len(rq) != 0:
            rqe = rq[0]
            if lqe > rqe:
                heapq.heappop(lq)
                heapq.heappop(rq)
                heapq.heappush(lq, rqe * -1)
                heapq.heappush(rq, lqe)
        
        print(lq[0] * -1)
        # print(lq)
        # print(rq)
        # print()