def sub_sort(A: list[int]):
    if len(A) <= 1:
        return -1
    
    unsorted_start = len(A) - 1
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            unsorted_start = i
            break
    
    unsorted_end = 0
    for i in range(len(A) - 1, 0, -1):
        if A[i] < A[i - 1]:
            unsorted_end = i
            break
            
    if unsorted_start > unsorted_end:
        return -1
    
    min_unsorted = min(A[unsorted_start:unsorted_end+1])
    max_unsorted = max(A[unsorted_start:unsorted_end+1])
    
    for i in range(unsorted_start):
        if A[i] > min_unsorted:
            unsorted_start = i
            break
        
        
    for i in range(len(A) - 1, unsorted_end - 1, -1):
        if A[i] < max_unsorted:
            unsorted_end = i
            break
        
    print(A)
    print(unsorted_start, unsorted_end)
    print()
    
a = [1,2,4,7,10,11,7,12,6,7,16,18,19]
sub_sort(a)

a = [2,4,6,1,3,5]
sub_sort(a)

a = [2,4,6,1,3,5,6]
sub_sort(a)

a = [0,2,4,6,1,3,5,6]
sub_sort(a)

a = [1,2,3,5,4,6,7,8]
sub_sort(a)

a = [1,2,3,6,5,4,7,8,9]
sub_sort(a)