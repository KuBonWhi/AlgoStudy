def solution(n, lost, reserve):
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)

    for i in reserveSet:
        if i-1 in lostSet:
            lostSet.remove(i-1)
        elif i+1 in lostSet:
            lostSet.remove(i+1)

    return n-len(lostSet)