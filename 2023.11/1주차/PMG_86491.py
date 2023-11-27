def solution(sizes):
    widthArr = []
    heightArr = []
    
    for size in sizes:
        widthArr.append(min(size))
        heightArr.append(max(size))
    
    return max(widthArr)*max(heightArr)