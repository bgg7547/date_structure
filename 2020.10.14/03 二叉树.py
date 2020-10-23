class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Node({self.data})"
#
class Tree:
#     def __init__(self):
#         self.root = None
#     #插入
#     def insert(self,data):
#         node = Node(data)
#         if self.root is None:
#             self.root = node
#         else:
#             temp = [self.root]
#             while True:
#                 pop_node = temp.pop(0)
#                 if pop_node.left is None:
#                     pop_node.left = Node
#                     return
#                 elif pop_node.right is None:
#                     pop_node.right = node
#                     return
#                 else:
#                     temp.append(pop_node.left)
#                     temp.append(pop_node.right)

    #二分搜索树
    def __init__(self):
        self.root = None
    def insert(self,data):
        node = Node(data)
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


t = Tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
print(t.root.right.left)

