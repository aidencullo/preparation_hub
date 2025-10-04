class List:
    
    def __init__(self, n):
        self.n = n
        self.items = list(range(n))

    def __getitem__(self, i):
        return self.items[i]

l = List(10)
assert l[0] == 0
assert l[1] == 1

