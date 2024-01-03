def get_line_coefficients(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    a = (y2 - y1) / (x2 - x1)
    b = a * x1 - y1
    
    return a, b

def best_line(points):
    line_count = {}
    
    for i in range(len(points) - 1):
        p1 = points[i]
        for j in range(i + 1, len(points)):
            p2 = points[j]
            
            a, b = get_line_coefficients(p1, p2)
            
            if (a, b) not in line_count:
                line_count[(a, b)] = 0
            line_count[(a, b)] += 1
            
    print(line_count)
    max_count = 0
    line = None, None
    for l, count in line_count.items():
        if count > max_count:
            max_count = count
            line = l
            
    print(line, ':', max_count)
    
points = [(0,0),(1,1),(2,3),(4,0),(6,9),(12,18)]
best_line(points)
            
            