def solution(friends, gifts):
    n = len(friends)
    cnt_list = []
    gift_pnt = [0 for i in range(n)]
    next_m = [0 for i in range(n)]   
    
    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        cnt_list.append(line)
    
    for gift in gifts:
        a, b = gift.split()
        i = friends.index(a)
        j = friends.index(b)
        cnt_list[i][j] += 1
        cnt_list[j][i] -= 1
        gift_pnt[i] += 1
        gift_pnt[j] -= 1
    
    for i in range(n):
        for j in range(i, n):
            if i != j:
                if cnt_list[i][j] < cnt_list[j][i]:
                    next_m[j] +=1
                elif cnt_list[i][j] > cnt_list[j][i]:
                    next_m[i] +=1
                else:
                    if gift_pnt[i] < gift_pnt[j]:
                        next_m[j] +=1
                    elif gift_pnt[i] > gift_pnt[j]:
                        next_m[i] +=1
    return max(next_m)