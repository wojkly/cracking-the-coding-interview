def is_substring(haystack, needle):
    return needle in haystack

def is_rotation(s1, s2):
    return is_substring(s2 + s2, s1)
    
    
assert is_rotation('waterbottle', 'erbottlewat') == True
assert is_rotation('waterbottel', 'erbottlewat') == False