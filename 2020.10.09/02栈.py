# # 数组实现栈
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     #压栈
#     def push(self,data):
#         self.stack.append(data)
#         self.size += 1
#
#     #弹栈
#     def pop(self):
#         if self.stack:
#             temp = self.stack.pop()
#             self.size -= 1
#         else:
#             raise IndexError('索引越界')
#         return temp
#
#     #栈顶元素
#     def peek(self):
#         if self.stack:
#             return self.stack[-1]
#
#     #是否为空
#     def is_empty(self):
#         if self.stack:
#             return False
#         return True
#
#     #长度
#     def chang(self):
#         return self.size
#
# stack = Stack()
# for i in range(5):
#     stack.push(i)
# print(stack)
# print(stack.pop())
# print(stack.is_empty())
# print(stack.chang())

#链表实现栈
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class linkstack:
    def __init__(self):
        self.top = None
        self.size = 0

    # 压栈   （相当于头部插入节点）
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    #弹栈
    def pop(self):
        if self.top is None:
            raise Exception("空列表")
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.size -= 1
        return temp



