def solution(N, stages):
    result = []
    answer = []
    for i in range(1, N + 1):
        clear = 0
        for j in stages:
            if j >= i:
                clear += 1
        unclear = stages.count(i)
        if clear == 0:
            failure = 0
        else:
            failure = unclear / clear
        result.append((i, failure))
    result.sort(key = lambda x: (-x[1], x[0]))
    for i in result:
        answer.append(i[0])
    return answer

