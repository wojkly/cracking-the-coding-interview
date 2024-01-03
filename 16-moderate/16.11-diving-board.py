def lengths(K: int, shorter, longer):
    length = K * shorter
    result = [length]
    for i in range(K):
        length += longer - shorter
        result.append(length)
        
    print(result)
    
lengths(5,7,9)