from heapq import *

def makeNewFood(first, second):
    return first + (second*2)

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville:
        if scoville[0] >= K:
            break
        if len(scoville)==1:
            if scoville[0] <= K:
                return -1
        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, makeNewFood(first, second))
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 7))