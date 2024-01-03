def smallest_diff(a, b):
    a.sort()
    b.sort()
    
    #merge
    i = 0
    j = 0
    smallest_diff = float('inf')
    s_i = -1
    s_j = -1
    
    while i < len(a) and j < len(b):
        curr_diff = abs(a[i] - b[j])
        if curr_diff < smallest_diff:
            smallest_diff = curr_diff
            s_i = a[i]
            s_j = b[j]
            
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
            
    print(s_i, s_j, smallest_diff)
    
a = [1,3,15,11,2]
b = [23,127,235,19,8]

smallest_diff(a,b)