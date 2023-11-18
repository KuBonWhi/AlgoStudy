from itertools import permutations


def solution(k, dungeons):
    answer = []

    for dungeon in permutations(dungeons):
        nowK = k
        cnt = 0
        for [limitK, usedK] in dungeon:
            if limitK <= nowK:
                nowK -= usedK
                cnt += 1

        answer.append(cnt)

    return max(answer)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
