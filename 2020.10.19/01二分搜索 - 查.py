
class BST:
    def __init__(self):
        self.root = None

    def seach(self,data):
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = temp
                else:
                    temp = temp.left
            else:
                if data > temp.data:
                    if temp.right is None:
                        temp.right = temp
                    else:
                        temp = temp.right

    # 遍历
    # 前序
    def preorder(self,node):
        stack = [node]
        while stack:
            pop_node = stack.pop()
            print(pop_node.data)
            if pop_node.right:
                stack.append(pop_node.right)
            if pop_node.left:
                stack.append(pop_node.left)
    # 中序
    def inorder(self,node):
        stack = []
        while node or len(stack) > 0:
            while node:
                if node:
                    stack.append(node)
                    node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node)
                node = node.right
    # houxu
    def postorder(self,node):
        stack1 = [node]
        stack2 = []
        while stack1:
            pop_node = stack1.pop()
            if pop_node.left:
                stack1.append(pop_node.left)
            if pop_node.right:
                stack1.append(pop_node.right)
            stack2.append(pop_node)
        while stack2:
            print(stack2.pop().data)



