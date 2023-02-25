# Miller–Rabin primality test
# Reference : https://seokjin2.tistory.com/6

# if (2 * area + 1) is primary number then no (x, y) pair exist 


DO_LOG = 1
DO_VERBOSE = 0

def dprt(log):
    if DO_LOG:
        print(log)

def vprt(log):
    if DO_VERBOSE:
        print(log)


# Fast power fucntion
def mod_power(x : int, y : int, m : int) -> int:
    res : int = 1
    x = x % m
    while y > 0:
        if y % 2 == 1:
            res = int((res * x) % m)
            y -= 1

        y = int(y / 2)
        x = (x * x) % m
    return res

def miller_rabin(num : int, p : int):
    vprt(f'num : {num} p : {p}')

    r : int = 0
    d : int = num - 1
    while d % 2 == 0:
        r += 1
        d = int(d / 2)
        
    vprt(f'r : {r} d : {d}')
    
    x : int = mod_power(p, d, num)
    vprt(f'x : {x}')
    
    if x == 1 or x == num - 1:
        return True
    
    for i in range(r - 1):
        x = mod_power(x, 2, num)
        vprt(f'Round : {i},  x : {x}')
        if x == num - 1:
            return True
    return False


def is_primary(num : int):
    vprt(f'[Primary test for {num}]')
    if num != 2 and num % 2 == 0:
        return False
    if num == 1:
        return False
    
    # Miller-Rabin primality test
    primary_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    
    for p in primary_list:
        vprt(f'{p} {num}')
        if num == p:
            return True
        else:
            if not miller_rabin(num, p):
                return False
    return True
    
def check_available(area):
    if is_primary(area * 2 + 1):
        return True
    else:
        return False

def primary_check_func_test():
    for i in range(20):
        if is_primary(i):
            dprt(f'{i} is prime\n')
        else:
            dprt(f'{i} is not prime\n')

if __name__ == "__main__":
    # primary_check_func_test()

    ans = 0
    problem_num = int(input())
    for i in range(problem_num):
        area = int(input())
        if check_available(area):
           ans += 1
    print(ans)
