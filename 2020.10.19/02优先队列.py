class PreQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self,data):
        self.array.append(data)
        self.size += 1
        self.up_heapfy()

    def up_heapfy(self):
        index = len(self.array) - 1
        while index > 0:
            parent_index = (index - 1) >> 1
            if self.array[index] > self.array[parent_index]:
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                index = parent_index
            else:
                break

        # -----------2
        # index = len(self.array) - 1
        # parent_index = (index - 1) >> 1
        # new = self.array[index]
        # while index > 0 and new > self.array[parent_index]:
        #     self.array[index] = self.array[parent_index]
        #     index = parent_index
        #     parent_index = (index - 1) >> 1
        # self.array[index] = new

    # def swap(self, index, parent_index):
    #     pass

    def remove(self,data):
        self.array[0] = self.array[-1]
        self.array.pop()
        self.size -= 1
        self.down_heapfy(0)
    def __repr__(self):
        return str(self.array)

    def down_heapfy(self,index):
        total_index = len(self.array) - 1
        while True:
            max_index = index
            if index * 2 + 1 <= total_index and self.array[index * 2 + 1] > self.array[max_index]:
                max_index = index * 2 + 1
            if index * 2 + 2 <= total_index and self.array[index * 2 + 2] > self.array[max_index]:
                max_index = index * 2 + 2
            if max_index == index:
                break
            self.array[index],self.array[max_index] = self.array[max_index],self.array[index]
            index = max_index


p = PreQueue()
p.enqueue(4)
p.enqueue(9)
p.enqueue(8)
p.enqueue(7)
p.enqueue(6)
print(p)
p.remove(7)
print(p)


