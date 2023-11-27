def solution(number, k):
    answer = []
    before = 0
    
    for n in number:
        while answer and k>0 and answer[-1] < n:
            k-=1
            answer.pop()
        answer.append(n)
        
    return ''.join(answer[:len(answer)-k])