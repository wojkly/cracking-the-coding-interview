def max_sequence_sum(a: list[int]):
    
    max_sum = -1
    max_sequence = []
    
    current_sum = 0
    current_sequence = []
    
    for n in a:
        current_sum += n
        
        if current_sum > max_sum:
            max_sum = current_sum
            current_sequence.append(n)
            max_sequence = current_sequence
        elif current_sum > 0:
            current_sequence.append(n)
        else:
            current_sum = 0
            current_sequence = []
            
    print(max_sum, ':', max_sequence)
    
a = [2,-8,3,-2,4,-10]
max_sequence_sum(a)
            
            