from typing import List
# 创建节点
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)

class Linklist:
    def __init__(self):
        self.head = None

    # 插入头部
    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    # 插入尾部
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # 位置插入
    def insert(self,i,data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            pre = temp
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp

    #删除
    #删除头部
    def pop_head(self):
        if self.head:
            self.head = self.head.next
    # 删除尾部
    def pop_wei(self):
        temp = self.head
        if temp:
            if temp.next:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
            else:
                self.pop_head()
        else:
            print('空链表')
    # 输出
    def __repr__(self):
        str = ""
        temp = self.head
        while temp:
            str += "{} --> ".format(temp)
            temp = temp.next
        return str + "END"

    #列表转链表
    def linklist(self,object: List):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next

l = Linklist()
l.insert_head(1)
l.append(2)
l.append(3)
l.insert(3,2.5)

print(l)
l.pop_head()
l.pop_wei()
print(l)
ll = Linklist()
ll.linklist([1,2,3,4,5,6])
print(ll)