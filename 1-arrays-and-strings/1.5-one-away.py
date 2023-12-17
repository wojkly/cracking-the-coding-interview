def one_or_zero_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    startErrorIndex = 0
    while startErrorIndex < len(s1) and startErrorIndex < len(s2) and s1[startErrorIndex] == s2[startErrorIndex]:
        startErrorIndex += 1
    
    s1Index = startErrorIndex
    s2Index = startErrorIndex
    
    if s1Index == len(s1) and s2Index == len(s2):
        #no operation needed
        return True
    
    if len(s1) == len(s2):
        #replace
        s1Index += 1
        s2Index += 1
    elif len(s1) > len(s2):
        #add letter to s2 (skip next letter in s1)
        s1Index += 1
    else:
        #add letter to s1 (skip next letter in s2)
        s2Index += 1
        
    
    while s1Index < len(s1) and s2Index < len(s2) and s1[s1Index] == s2[s2Index]:
        s1Index += 1
        s2Index += 1
        
    return s1Index == len(s1) and s2Index == len(s2)

assert one_or_zero_away('pale', 'ple') == True
assert one_or_zero_away('pales', 'pale') == True
assert one_or_zero_away('pale', 'bale') == True
assert one_or_zero_away('pale', 'bake') == False

assert one_or_zero_away('essa', 'essasito') == False