# 数组实现栈
# class ArrayStack:
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
#             raise Exception("空栈")
#
#     #栈顶元素
#     def peek(self):
#         return self.stack[-1]
#
#     #是否空
#     def is_empty(self):
#         return bool(self.stack)
#
#     #输出
#     def out(self):
#         for i in self.stack:
#             print(i)

# 链表实现栈
class Node:
    def __init__(self,data):
        self.data = data


class Stack:
    pass

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.peek())
# print(s.is_empty())
# s.out()
