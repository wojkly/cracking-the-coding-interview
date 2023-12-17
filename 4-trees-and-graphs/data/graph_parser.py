class GraphParser:
    def parse(file_path):
        vertices = []
        
        with open(file_path) as f:
            n = int(f.readline())
            directed = f.readline().find('DIRECTED') != -1
            
            vertices = [set() for _ in range(n)]
            
            for line in f.readlines():
                v, u = line.split(' ')
                v, u = int(v), int(u)
                
                vertices[v].add(u)
                if not directed:
                    vertices[u].add(v)
                    
        return vertices
            