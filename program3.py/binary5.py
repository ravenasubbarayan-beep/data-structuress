class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def evaluate(root):
    if root.left is None and root.right is None:
        return int(root.data)

    a = evaluate(root.left)
    b = evaluate(root.right)

    if root.data == '+':
        return a + b
    if root.data == '-':
        return a - b
    if root.data == '*':
        return a * b
    if root.data == '/':
        return a / b

# Expression: (6 + 2) * (5 - 3)
root = Node('*')

root.left = Node('+')
root.right = Node('-')

root.left.left = Node('6')
root.left.right = Node('2')

root.right.left = Node('5')
root.right.right = Node('3')

print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nEvaluation:", evaluate(root))