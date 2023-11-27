def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            width = yellow / i
            height = i
            if (width*2 + height*2 + 4) == brown:
                answer.append(width+2)
                answer.append(height+2)
                break
    
    return answer
