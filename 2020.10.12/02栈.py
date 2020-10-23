class StackOfArray:
    def __init__(self):
        self.stack = []
        self.size = 0
    #压栈    往后增加元素
    def push(self,data):
        self.stack.append(data)
        self.size += 1
    #弹栈
    def pop(self):
        self.stack.pop()
        self.size -= 1

    #栈顶
    def peek(self):
        return self.stack[-1]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackOfLinklist:
    def __init__(self):
        self.top = None
        self.size = 0

    #压栈   往头部插入节点 后进先出
    def push(self,data):
        node = Node(data)
