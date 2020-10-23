# 节点
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):            #对象 --> 字符串
        return f"Node({self.data})"

class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 索引
    def get(self,index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    #插入
    def insert(self,index,data):
        new_node = Node(data)
        if index < 0 or index > self.size: #越界
            raise Exception("索引越界")
        elif self.size == 0:              #空链表
           self.head = new_node
           self.tail = new_node
        elif index == 0:                #头部插
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:          #尾部插
            self.tail.next = new_node
            self.tail = new_node
        else:                             #中间插
            pre = self.get(index - 1)
            new_node.next = pre.next
            pre.next = new_node

        self.size += 1
    # 删除
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        remove_node = self.get(index)
        if index == 0:      #删除头
            self.head = self.head.next
        elif index == self.size - 1:  #删除尾
            pre = self.get(index - 1)
            pre.next = None
            self.tail = pre
        else:
            pre = self.get(index - 1)
            pre.next = pre.next.next
        self.size -= 1
        return remove_node

    # 翻转链表


    def __repr__(self):
        string = ""
        temp = self.head
        while temp:
            string += f"{temp} --> "
            temp = temp.next
        return string + "END"

l = Linklist()
l.insert(0,1)
l.insert(0,2)
l.insert(1,3)
l.insert(0,4)
l.insert(4,5)
print(l)
l.remove(4)
print(l)







