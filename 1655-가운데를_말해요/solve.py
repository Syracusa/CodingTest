# Use 2 priority queue
# Max Heap & Min Heap
# Priority queue API is slow. use heapq

import sys
import heapq

if __name__ == "__main__":
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