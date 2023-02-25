# Main 함수 지정
```py
if __name__ == "__main__":
    somethingtodo()
```


# 입출력

## Basic 
```py
a, b = map(int, input().split())
print(a+b)
```

## From file
```py
import sys
sys.stdin = open("input.txt", "r")
```

## Line to int
```py
N = int(input())
print(N)
```

## Chars split with blank
```py
input().split()
```

## Ints split by blank
```py
N,M = map(int, input().split())
```

## 1-dimension arr
```py
arr = list(map(int, input().split()))
```

## String to char list
```py
arr = list(input())
```

## String to int list
```py
arr = list(map(int, input()))
```

## N-line 2-dimension arr
```py
arr = [list(map(int, input().split())) for _ in range(N)]
```

## Copy 2-dimension arr
```py
arr2 = [l[:] for l in arr]
```

## Length of array
```py
arrlen = len(arr)
```

## range()
```py
range(start, stop, step)
```

## 기타
+ 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용
+ 단 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함꼐 사용함


# Snippet
+ Fast power fucntion
```py
def mod_power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            res = (res * x) / p
            y -= 1

        y /= 2
        x = (x * x) % p
    return res
```