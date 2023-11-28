def solution(answers):
    random1 = [1,2,3,4,5]
    random2 = [2,1,2,3,2,4,2,5]
    random3 = [3,3,1,1,2,2,4,4,5,5]
    randomResult = [[1,0],[2,0],[3,0]]
    maxCnt = 0
    
    for i, answer in enumerate(answers):
        if answer == random1[i%len(random1)]:
            randomResult[0][1] += 1
        if answer == random2[i%len(random2)]:
            randomResult[1][1] += 1
        if answer == random3[i%len(random3)]:
            randomResult[2][1] += 1
        if i == len(answers)-1:
            maxCnt = max(randomResult[0][1], randomResult[1][1], randomResult[2][1])
    
    return [i for [i, cnt] in randomResult if cnt == maxCnt]