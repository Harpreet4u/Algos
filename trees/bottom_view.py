# bottom view of a tree
# O(V+E) or O(n)

# maintain distance from root as dist-1 and dist+1 (dist=0 for root)
class Node:
    
    def __init__(self):
        self.val = None
        self.dist = 0
        self.left = None
        self.right = None

def view(node):

    if not node:
        return
    
    hash  = {}
    queue = []

    node.dist = 0
    queue.append(node)

    while len(queue) != 0:

        front = queue[0]
        queue.pop()

        dist = front.dist

        hash[dist] = front.val

        if front.left:
            front.left.dist = dist - 1
            queue.append(front.left)
        if front.right:
            front.right.dist = dist + 1
            queue.append(front.right)

        
    for k, v in hash:
        print v

