# lca for Binary tree.
# O(h)


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca_util(root, n1, n2, v):

    if root is None:
        return None

    if root.data == n1:
        v[0] = True
        return root

    if root.data == n2:
        v[1] = True
        return root

    left = lca_util(root.left, n1, n2, v)
    right = lca_util(root.right, n1, n2, v)
    

    if left and right:
        return root

    return left if left else right


def find(root, v):

    if not root:
        return False
    
    if root.data == v or find(root.left, v) or find(root.right, v):
        return True

    return False

def lca(root, n1, n2):
    v = [False, False]
    lca = lca_util(root, n1, n2, v)

    if (v[0] and v[1]) or v[0] and find(lca, n2) or v[1] and find(lca, n1):
        return lca

    return None

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    assert lca(root, 4, 5).data == 2
    assert lca(root, 4, 10) == None
