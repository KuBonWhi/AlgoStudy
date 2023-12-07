def solution(nums):
    typeCnt = len(set(nums))
    selectCnt = len(nums)//2

    if typeCnt > selectCnt:
        return selectCnt
    
    return typeCnt

print(solution([3,1,2,3]))