from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)
class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def __insert(self,data):
        node = Node(data,None)
        if self.root is None:
            self.root = node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right
            node.parent = parent_node

    def insert(self,*data):
        for i in data:
            self.__insert(i)
        return self

    def search(self,data):
        if self.root is None:
            raise IndexError("空树")
        else:
            node = self.root
            while node and node.data != data:
                if data < node.data:
                    node = node.left
                else:
                    node = node.right
            # print(node)
            return node

    def remove(self,data):
        node = self.search(data) #找到节点
        if node.left is None and node.right is None:
            self.__seassign(node,None)
        elif node.left is None:
            self.__seassign(node,node.right)
        elif node.right is None:
            self.__seassign(node,node.left)
        else:
            temp = self.max_node(node.left)
            self.remove(temp.data)
            node.data = temp.data

    def __seassign(self, node, new_child):
        if new_child is not None:      #替换的找父节点
            new_child.parent = node.parent

        if node.parent is not None:    #父节点找到替换的
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child


    def max_node(self,node):
        # if left is None:
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node


    def is_right(self, node):
        return node.parent.right == node

    def is_empty(self):
        return not self.root

    # -------------------遍历
    #   前序 (递归）
    def presort(self,node):
        if not node:
            return None
        print(node.data)
        self.presort(node.left)
        self.presort(node.right)

    # 栈实现前序
    def preOrderTraverse(self,node):
        stack = [node]
        while len(stack) > 0:
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()
    # 中序遍历
    def minOrderTraversr(self,node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.data)
                node = node.right

bst = BST()
bst.insert(8,3,1,6,10)
print(bst)
bst.minOrderTraversr(bst.root)
# bst.remove(3)
# print(bst)

