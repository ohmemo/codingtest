def solution(number, n, m):
    return int((number%n == 0)&(number%m == 0)&(number!= 1))