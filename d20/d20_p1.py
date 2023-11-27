input = "input.txt"

class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None
x = [Node(int(x)) for x in open(input).readlines()]

for i in range(len(x)):
    if i == len(x) - 1:
        x[i].right = x[0]
        x[i].left = x[i-1]
    else:
        x[i].right = x[i+1]
        x[i].left = x[i-1]


def printer(x):
    for i in range(len(x)):
        print(x[i].left.n, x[i].n, x[i].right.n)
        
m = len(x) - 1
for node in x:
    if node.n == 0:
        zero = node
        continue
    r = node
    if node.n > 0:
        for _ in range(node.n % m):
            r = r.right
    else:
        for _ in range((-node.n + 1) % m):
            r = r.left
    if node == r:
        continue
    node.left.right = node.right
    node.right.left = node.left
    r.right.left = node
    node.right = r.right
    r.right = node
    node.left = r

s = 0
for _ in range(3):
    for _ in range(1000):
        zero = zero.right
    s += zero.n
print(s)
