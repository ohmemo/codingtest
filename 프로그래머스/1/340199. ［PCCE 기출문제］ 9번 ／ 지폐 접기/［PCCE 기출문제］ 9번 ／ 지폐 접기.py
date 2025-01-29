def solution(wallet, bill):
    answer = 0
    cnt = 1
    while cnt:
        if ((wallet[0] >= bill[0])&(wallet[1] >= bill[1]))|((wallet[0] >= bill[1])&(wallet[1] >= bill[0])):
            cnt = 0
        else:
            bill[bill.index(max(bill))] = bill[bill.index(max(bill))] // 2
            answer += 1
    return answer