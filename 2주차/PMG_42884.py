def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    print(routes)
    
    beforeEnd = -30001
    for start, end in routes:
        if beforeEnd < start:
            answer += 1
            beforeEnd = end
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))