def solution(n, numlist):
    answer = []
    for number in numlist:
        if number % n == 0:
            answer.append(number)
    return answer