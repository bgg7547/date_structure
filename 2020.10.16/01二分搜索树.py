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
        return pformat("%s"%{(self.data): (self.left,self.right)})


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not bool(self.root)

    def __insert(self,data):
        node = Node(data,None)
        if self.is_empty():
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

    def reseach(self,data):
        if self.is_empty():
            raise IndexError("空树")
        else:
            temp = self.root
            while temp:
                if data < temp.data:
                    temp = temp.left
                elif data > temp.data:
                    temp = temp.right
                else:
                    return temp

    def remove(self,data):
        node = self.reseach(data)
        if node.left is None and node.right is None:
            self.__seassgin(node,None)
        elif node.left is None:
            self.__seassgin(node,node.right)
        elif node.right is None:
            self.__seassgin(node,node.left)
        else:
            temp = self.max_node(node.left)
            self.remove(temp.data)
            node.data = temp.data



    def __seassgin(self, node, new_child):
        if new_child is not None:
            new_child.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = node

    def max_node(self, node):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return  node

    def is_right(self,node):
        return node.parent.right == node

    def __repr__(self):
        return str(self.root)

    def preorder(self,node):
        stack = [node]
        while len(stack) > 0:
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def inorder(self,node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) >0:
                node = stack.pop()
                print(node.data)
                node = node.right
    # def inorder(self,node):
    #     if node is None:
    #         return None
    #     print(node.data)
    #     self.inorder(node.left)
    #     self.inorder(node.right)
    def post_order_stack(self,node):
        if node is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            pop_node = stack1.pop()
            if pop_node.left:
                stack1.append(pop_node.left)
            if pop_node.right:
                stack1.append(pop_node.right)
            stack2.append(pop_node)
        while stack2:
            print(stack2.pop().data)
    #层序
    def cenxu(self,node):
        if node is None:
            raise IndexError("kongshu")
        else:
            queue = [node]
            while queue:
                pop_node = queue.pop(0)
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
                print(pop_node.data)


bst = BST()
bst.insert(8,3,1,6,10)
print(bst)
# bst.remove(3)
# print(bst)
# bst.preorder(bst.root)
# bst.inorder(bst.root)
# bst.post_order_stack(bst.root)
bst.cenxu(bst.root)


