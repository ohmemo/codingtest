def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    time = 0
    continuous_time = 0
    attack_index = 0

    for attack_time, damage in attacks:
        # 붕대 감기 동안 체력 회복 (공격까지의 시간)
        while time < attack_time:
            time += 1
            continuous_time += 1

            if health <= 0:
                return -1

            # 1초마다 회복
            health = min(health + x, max_health)

            # t초 연속 성공 시 추가 회복
            if continuous_time == t:
                health = min(health + y, max_health)
                continuous_time = 0

        # 몬스터 공격 처리
        health -= damage
        if health <= 0:
            return -1

        # 연속 붕대 감기 초기화
        continuous_time = 0
        time += 1

    return health
