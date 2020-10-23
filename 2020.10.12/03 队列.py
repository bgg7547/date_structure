#                队列：先进先出，后进后出

# # 数组实现队列
# class Queue:
#     def __init__(self):
#         self.entries = []
#         self.size = 0
#
#     # 入队
#     def enqueue(self,data):
#         self.entries.append(data)
#         self.size += 1
#
#     # 出队
#     def dequeue(self):
#         temp = self.entries[0]
#         self.entries = self.entries[1:]
#         self.size -= 1
#         return temp
#
#     #查找
#     def indexGet(self,index):
#         return self.entries[index]
#
#     #倒序
#     def reverse(self):
#         self.entries = self.entries[::-1]
#     #输出
#     def __repr__(self):
#         return "<" + str(self.entries)[1:-1] + ">"

#链表实现
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class LinkQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #入队
    def enqueue(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    # 出队
    def dequeue(self):
        pop_node = self.head
        if self.is_empty():
            raise IndexError("空队")
        else:
            self.head = self.head.next
            pop_node.next = None
        self.size -= 1
        return pop_node

    def is_empty(self):
        return self.head is None

    def __repr__(self):
        cur = self.head
        string = ""
        while cur:
            string += f"{cur} --> "
            cur = cur.next
        return string + "END"


q = LinkQueue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
q.dequeue()
# print(q)
# print(q.indexGet(2))
# q.reverse()
print(q)
