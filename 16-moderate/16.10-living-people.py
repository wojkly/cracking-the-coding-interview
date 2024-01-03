def living_people(b: list, d: list):
    b.sort()
    d.sort()
    
    print(b)
    print(d)
    
    #merge
    curr_living_count = 0
    
    max_living_year = b[0]
    max_living_count = 0
    
    i,j = 0,0
    
    while i < len(b) and j < len(d):
        curr_year = min(b[i], d[j])
        #birth all in current year
        while i < len(b) and b[i] == curr_year:
            curr_living_count += 1
            i += 1
        
        #set max count
        if curr_living_count > max_living_count:
            max_living_count = curr_living_count
            max_living_year = curr_year
        
        #die all in current year
        while j < len(d) and d[j] == curr_year:
            curr_living_count -= 1
            j += 1
            
    print(max_living_year, ':', max_living_count)
        


b = [1924, 1919, 1987, 1959, 1922, 1979, 1916, 1925, 1905, 1992]
d = [1929, 1935, 2046, 2048, 1995, 2001, 1982, 2014, 1923, 2010]
living_people(b, d)

b = [1,2,3,5,5,5,5,10]
d = [5,5,5,5,5,5,10,10]
living_people(b, d)
# from random import randint
# b = [randint(1900,2000) for _ in range(10)]
# print('b =', b)
# print('d =',[p + randint(1,100) for p in b])