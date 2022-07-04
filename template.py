# basic 
a, b = map(int, input().split())
print(a+b)

# from file
import sys
sys.stdin = open("input.txt", "r")

# Line to int
N = int(input())
print(N)

# Chars split with blank
input().split()

# Ints split by blank
N,M = map(int, input().split())

# 1-dimension arr
arr = list(map(int, input().split()))

# String to char list
arr = list(input())

# String to int list
arr = list(map(int, input()))

# N-line 2-dimension arr
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열 복사
arr2 = [l[:] for l in arr]

# 배열의 길이
arrlen = len(arr)

# range함수
range(start, stop, step)

#파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용
#단 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함꼐 사용함