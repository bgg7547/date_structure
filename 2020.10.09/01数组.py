class Array:
    def __init__(self,capacity):
        self.array = [None] * capacity
        self.size = 0

    #插入
    def insert(self,index,element):
        if index < 0 :
            raise IndexError("索引越界")
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1,-1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    #扩容
    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    #删除
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("索引越界")

        for i in range(index,self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    #输出
    def out(self):
        for i in range(self.size):
            print(self.array[i],end="->")

list = Array(4)
list.insert(0,1)
list.insert(0,2)
list.insert(0,3)
list.insert(0,4)
list.insert(0,5)
list.remove(3)
list.out()

#判断环
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return f"Node{self.data}"
# def iscircle(head: Node):
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             # return True
#             break
#     slow = head
#     while slow != fast:
#         slow = slow.next
#         fast = fast.next
#     return slow
#
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n3
# print(iscircle(n1))






