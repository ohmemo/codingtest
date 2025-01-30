def can_place_mat(park, x, y, size):
    """
    주어진 (x, y) 위치에서 size x size 크기의 돗자리를 깔 수 있는지 확인
    """
    n, m = len(park), len(park[0])
    if x + size > n or y + size > m:
        return False
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if park[i][j] != "-1":
                return False
    return True

def solution(mats, park):
    mats.sort(reverse=True)  # 큰 돗자리부터 시도
    n, m = len(park), len(park[0])
    
    for size in mats:
        for i in range(n):
            for j in range(m):
                if can_place_mat(park, i, j, size):
                    return size
    
    return -1