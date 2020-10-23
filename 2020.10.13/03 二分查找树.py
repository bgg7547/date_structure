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

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #是否为空
    def is_empty(self):
        return not bool(self.root)

    #插入
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

    def insert(self,*datas):
        for data in datas:
            self.__insert(data)
        return self

    #判断右节点
    def is_right(self,node):
        return node == node.parent.right

    #删除
    def remove(self,data):
        node = self.search(data)
        if node is not None:
            if node.left is None and node.right is None:
                self.__seassign_nodes(node,None)
            elif node.left is None:
                self.__seassign_nodes(node,node.right)
            elif node.right is node:
                self.__seassign_nodes(node,node.left)
            else:
                max_node = self.lmax_node(node.left)
                self.remove(max_node.data)
                node.data = max_node.data

    def __seassign_nodes(self, node, new_child):
        if new_child is not None:
            new_child.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child


    # 查找
    def search(self,data):
        if self.is_empty():
            raise IndexError("空树")
        else:
            node = self.root
            while node and node.data != data:
                if data < node.data:
                    node = node.left
                elif data > node.data:
                    node = node.right
            print(node)
            return node

    #输出
    def __repr__(self):
        return str(self.root)



    def lmax_node(self, node):
        pass


bst = BinarySearchTree().insert(2,5,3,2)
print(bst)