#encoding=utf8
"""
树形状:
     1
   3    2
 7  6  5 4
0


"""
class Node(object):

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


def bfs(tree):
    """

    :param tree:
    :return:
    """
    queue = []
    if tree ==None:
        return
    queue.append(tree)

    while queue:

        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        print node.data

def dfs(tree):
    """

    :param tree:
    :return:
    """
    if tree ==None:
        return
    print tree.data
    dfs(tree.left)
    dfs(tree.right)

def dfs12(tree):
    """

    :param tree:
    :return:
    """
    if not tree:
        return

    stack = []
    stack.append(tree)
    while stack:
        node = stack.pop()
        print node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def isSameTree(tree1,tree2):

    if not tree1 and not tree2:
        return True

    elif tree1 and tree2:
        return tree1.data ==tree2.data and isSameTree(tree1.left,tree2.left) and isSameTree(tree1.right,tree2.right)
    else:
        return False

dfs(tree)
dfs12(tree)