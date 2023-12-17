class StringBuilder:
    def __init__(self) -> None:
        self.data = []
    
    def add(self, s):
        self.data.append(s)
        
    def get(self):
        return ''.join(self.data)
    
sb = StringBuilder()
sb.add('essa')
sb.add('sito')
print(sb.get())
sb.add('essa')
sb.add('sito')
sb.add('essa')
sb.add('sito')
sb.add('essa')
sb.add('sito')
print(sb.get())