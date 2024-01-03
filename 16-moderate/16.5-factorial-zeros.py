def get_zeros(n: int) -> int:
    result = 0
    # count 10s
    # result += n // 10
    
    #count 5, 25, 125 etc...
    five_power = 5
    while five_power <= n:
        result += n // five_power
        five_power *= 5
        
    return result


factorial = 1
zeros = 0
for i in range(1,1001):
    factorial *= i
    while factorial % 10 == 0:
        zeros += 1
        factorial //= 10
    print('number: ',i,'zeros: ', zeros, 'predicted:', get_zeros(i))
    
    