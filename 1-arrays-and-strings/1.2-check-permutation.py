def check_permutation(s1, s2):
    occurences = {}
    for l in s1:
        if l in occurences:
            occurences[l] += 1
        else:
            occurences[l] = 1
            
    
    for l in s2:
        if l in occurences:
            occurences[l] -= 1
        else:
            return False
        
    for v in occurences.values():
        if v != 0:
            return False
    
    return True

assert check_permutation('abcdefgh', 'efcbdgha') == True
assert check_permutation('abcdefgh', 'efcbdha') == False
assert check_permutation('abcdefgaabh', 'efabacbdgha') == True
    