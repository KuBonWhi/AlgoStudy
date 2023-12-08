def solution(participant, completion):
    answer = ''
    participantMap = {}

    for p in participant:
        if p in participantMap:
            participantMap[p] += 1
        else:
            participantMap[p] = 1

    for c in completion:
        participantMap[c] -= 1
    
    for k, v in participantMap.items():
        if v == 1:
            answer = k

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))