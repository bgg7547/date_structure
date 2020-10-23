# 节点
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)
class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
    #插入   索引
    def insert(self,index,data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        elif self.size == 0:              # 空链表
            self.head = new_node
            self.tail = new_node
        elif index == 0:                 #头部插
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:          #尾部插
            self.tail.next = new_node
            self.tail = new_node
        else:                                #中间插
            pre = self.get(index - 1)
            new_node.next = pre.next
            pre.next = new_node
        self.size += 1

    # 删除
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception('索引越界')
        remove_node = self.get(index)
        if index == 0:
            self.head = self.head.next
        elif index == self.size - 1:
            self.tail = self.get(index - 1)
        else:
            pre = self.get(index - 1)
            pre.next = pre.next.next
        self.size -= 1
        return remove_node

    # 反转
    def reverse(self):
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre
    # 输出
    def __repr__(self):
        string = ""
        temp = self.head
        while temp:
            string += f"{temp} --> "
            temp = temp.next
        return string + "END"
    # 快慢指针

l = Linklist()
l.insert(0,1)
l.insert(1,2)
l.insert(2,3)
l.insert(2,4)
l.insert(4,5)
l.insert(4,5)
print(l)
l.reverse()
print(l)
