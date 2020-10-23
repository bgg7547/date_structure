class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Node({self.data})"
class Tree:
    def __init__(self):
        self.root = None

    #   插入
    def add(self,data):
        node = Node(data)
        if self.root is None:    #空树情况
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:    #判断左子树为空
                    pop_node.left = node
                    return
                elif pop_node.right is None:  #判断右子树为空
                    pop_node.right = node
                    return
                else:                         #都不为空
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    # 找父节点
    def get_parent(self,itmp):
        if self.root.data == itmp:
            return None
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == itmp:
                return pop_node
            if pop_node.right.data == itmp:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right   :
                temp.append(pop_node.right)
        return None

t = Tree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
t.add(6)
print(t.root.left.right)