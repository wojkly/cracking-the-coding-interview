def triple_step(n):
    possible_ways = [0 for _ in range(n+1)]
    #1 way to be at 0 step
    possible_ways[0] = 1
    
    #count ways to go 1,2,3 from each step itreratively
    
    for i in range(n):
        for step in range(1,4):
            if i + step <= n:
                possible_ways[i + step] += possible_ways[i]
                
    return possible_ways[n]

for i in range(1, 10):
    print("possible ways to go up ", i, " steps: ", triple_step(i))
    