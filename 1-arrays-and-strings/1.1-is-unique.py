def is_unique(s):
    dict = {}
    for l in s:
        if l in dict:
            return False
        dict[l] = True
    return True
    
assert is_unique('essa') == False 
assert is_unique('akap') == False  
assert is_unique('bruh') == True      
