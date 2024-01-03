def set_a_as_first(pattern: str) -> str:
    if pattern[0] == 'a':
        return pattern
    
    #starts with b...
    r = []
    for l in pattern:
        if l == 'a':
            r.append('b')
        else:
            r.append('a')
    return ''.join(r)

def is_matching(value: str, pattern: str, a: str, b: str) -> bool:
    i = 0
    
    for p in pattern:
        if p == 'a':
            m = a
        else:
            m = b
        
        next_i = i + len(m)
        if value[i:next_i] != m:
            return False
        
        i = next_i
        
    return True
        
    
def is_pattern(value: str, pattern: str):
    n = len(value)
    
    pattern = set_a_as_first(pattern)
    a_count = len(list(filter(lambda l: l == 'a', pattern)))
    b_count = len(list(filter(lambda l: l == 'b', pattern)))
    a_array = []
    b_pattern_index = pattern.find('b')
    
    for i, l in enumerate(value):
        a_array.append(l)
        
        b_length = (n - len(a_array) * a_count) // b_count
        
        if len(a_array) * a_count > n or  len(a_array) * a_count + b_length * b_count != n:
            continue
        
        b = value[len(a_array) * b_pattern_index : len(a_array) * b_pattern_index + b_length]
        
        a = ''.join(a_array)
        # print(a, b)
        
        if is_matching(value, pattern, a, b):
            return a, b
        
    return None
        
v = 'catcatgocatgogogocatcatgoccatcatgocatgogogoatgogogocatcatgocatgogogo'
p = 'aba'
r = is_pattern(v, p)
print(r)
        
        
        
        
    