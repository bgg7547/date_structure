
#节点
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)
class Linklist:
    def __init__(self):
        self.head = None
    #插头
    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    # 插尾
    def append(self):
         pass
    def __repr__(self):
        str = ""
        temp = self.head
        while temp:
            str += "{} --> ".format(temp)
            temp = temp.next
        return str + "END"

l = Linklist()
l.insert_head(3)
l.insert_head(3)
l.insert_head(2)
l.insert_head(1)
print(l)