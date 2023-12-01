# def solution(n, times):
#     times.sort()

#     answer = 0
#     start = times[0]
#     end = times[len(times)-1] * n
#     while start <= end:
#         cnt = 0
#         mid = (start+end)//2
#         for time in times:
#             cnt += mid//time
        
#         if cnt >= n:
#             answer = mid
#             end = mid - 1
#         else:
#             start = mid + 1

#     return answer
def solution(n, times):
    answer = 0
    m=1
    while 1:
        cnt = 0
        for time in times:
            cnt += m//time
        if cnt == n:
            answer = m
            break
        m += 1
    
    return answer

print(solution(6, [7, 10])) 