class List:
    
    def __init__(self, n):
        self.n = n
        self.k = 0
        self.items = list(range(n))

    def __getitem__(self, i):
        return self.items[self.index(i)]

    def index(self, i):
        return (i + self.k) % self.n

    def rotate(self, k):
        self.k += k
    

l = List(10)
assert l[0] == 0
assert l[1] == 1

l.rotate(1)
assert l[0] == 1
assert l[1] == 2


for i in range(10):
    assert l[i] == (i + 1) % 10

l.rotate(5)
assert l[0] == 6

l.rotate(50)
assert l[0] == 6
