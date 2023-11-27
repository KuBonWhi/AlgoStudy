from itertools import permutations

def checkPrime(n):
    if n == 0 or n == 1:
         return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numberSet = set()

    for i in range(1, len(numbers)+1):
        for number in permutations(numbers,i):
            num = int(''.join(number))
            numberSet.add(num)

    for num in numberSet:
        if checkPrime(num):
                answer += 1

    return answer


print(solution("011"))