class Array:
    def __init__(self,capacity):
        self.array = [None] * capacity   #列表容量
        self.size = 0         #有效长度

    # 插入
    def insert(self,index,element):
        if index < 0:
            raise IndexError("索引越界")
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1,index - 1,-1): #倒着遍历，正着会覆盖
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    # 删除
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("索引越界")
        for i in range(index,self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    # 扩容
    def addcapacity(self):
        # 创建新数组
        new_array = [None] * len(self.array) * 2
        # 往新数组添加原有元素
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    # 输出
    


