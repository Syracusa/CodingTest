# 약수찾기

import sys
import math

def get_divisors(num):
    if num == 1:
        return [1]
    l = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            l.append(i)
    
    llen = len(l)
    for i in range(llen):
        adiv = l[llen - i - 1]
        
        d = int(num / adiv)
        if adiv != d:
            l.append(d)
        
    return l

def print_correct(l):
    print(f'{l[len(l) - 1]} = ', end='')
    for i in range(len(l) - 2):
        print(f'{l[i]} + ', end='')
    print(f'{l[len(l) - 2]}')

if __name__ == "__main__":
    
    while True:
        num = int(sys.stdin.readline())
        if (num == -1):
            break
        
        if (num == 1):
            print('1 = 1')
            continue
        
        sum = 0
        divs = get_divisors(num)
        for i in range(len(divs) - 1):
            sum += divs[i]
        if sum == num:
            print_correct(divs)
        else:
            print(f'{num} is NOT perfect.')