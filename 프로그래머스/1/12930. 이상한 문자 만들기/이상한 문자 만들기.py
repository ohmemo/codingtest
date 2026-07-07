def solution(s):
    answer = ''
    for split_s in s.split(" "):
        for i in range(len(split_s)):
            if i % 2:
                answer += split_s[i].lower()
            else:
                answer += split_s[i].upper()
        if split_s != s.split()[-1]:
            answer += ' '
    return answer