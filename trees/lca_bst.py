# LCS in Binary Search Tree
# O(h) -> h is height of the tree
# Space Recursion stack
# iterative version constant space

class Tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lcs_recursive(root, n1, n2):

    if root is None:
        return None

    if root.data > n1 and root.data > n2:
        return lcs_recursive(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return lcs_recursive(root.right, n1, n2)

    return root


def lcs_iterative(root, n1, n2):

    while root != None:

        if root.data > n1 and root.data > n2:
            root = root.left
        elif root.data < n1 and root.data < n2:
            root = root.right
        else:
            break
    return root


if __name__ == '__main__':
    root = Tree(20)
    root.left = Tree(8)
    root.right = Tree(22)
    root.left.left = Tree(4)
    root.left.right = Tree(12)
    root.left.right.left = Tree(10)
    root.left.right.right = Tree(14)

    assert lcs_recursive(root, 10, 14).data == 12
    assert lcs_recursive(root, 14, 8).data == 8
    assert lcs_recursive(root, 10, 22).data == 20

    assert lcs_iterative(root, 10, 14).data == 12
    assert lcs_iterative(root, 14, 8).data == 8
    assert lcs_iterative(root, 10, 22).data == 20


