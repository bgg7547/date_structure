from typing import List
#  节点
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    # 重写输出方法
    def __repr__(self):
        return "Node({})".format(self.data)
# n = Node(1)
# print(n)


class Linklist:
    # 初始化头部
    def __init__(self):
        self.head = None

    # 插入头部
    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
    # 尾部插入

    def append(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # 输出
    def __repr__(self):
        string = ""
        # ------------------- 遍历链表
        temp = self.head
        while temp:
            string += "{} --> ".format(temp)
            temp = temp.next
        return string + "End"

    # 随机插入
    def insert(self, i, data):
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
    # 列表生成链表

    def linklist(self, object: List):
        # self.head = Node(object[0])
        # temp = self.head
        # for i in object[1:]:
        # node = Node(i)
        # temp.next = node
        # temp = temp.next
        #  2
        for i in object:
            self.append(i)

    # 删除
    # 删除头节点
    def pop_head(self):
        temp = self.head
        if temp:
            self.head = self.head.next
            temp.next = None

    # 删除尾节点
    def pop_wei(self):
        temp = self.head
        # 判断是否为空
        if temp:
            # 判断只有一个节点的情况
            if temp.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            print("空链表")

    # 根据值删除
    def pop(self,data):
        pre = Node(None)
        pre.next = self.head
        self.head = pre
        while pre.next:
            if pre.next.data ==data:
                pre.next = pre.next.next
            else:
                pre = pre.next
        self.head = self.head.next


    # 反转链表
    def relinklist(self):
        pre = None
        cur = self.head
        while cur:

            next_node = cur.next
            # 后节点指向前节点
            cur.next = pre
            # 存储节点的变量一起后移
            pre = cur
            cur = next_node
        # 重置头部
        self.head = pre

    #索引
    def getitem(self, index):
        if self.head is None:
            raise IndexError("konglianbiao")
        cur = self.head
        for _ in range(1,index):
            if cur.next is None:
                raise IndexError('越界')
            cur = cur.next
        return cur

    # 修改值
    def __setitem__(self, key, value):
        cur = self.head
        if cur is None:
            return "空链表"
        for _ in range(1,key):
            if cur.next is None:
                return "越界"
            cur = cur.next
        cur.data = value

l = Linklist()
l.insert_head(1)
l.append(2)
l.append(3)
l.insert(3, 2.5)
l.insert(5, 3.5)
print(l)
l.pop(3.5)
# l.pop(1)
# l.pop_wei()
# ll = Linklist()
# ll.linklist([1, 2, 3, 4, 5])
print(l)
# l.relinklist()
# print(l)
# print(l.getitem(1))

