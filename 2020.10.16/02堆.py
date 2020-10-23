class Heap:
    def __init__(self):
        self.heap = []

    # 返回父节点下标
    def get_parent_index(self,index):
        if index == 0 or index > len(self.heap) - 1:
            return 0
        else:
            return (index - 1) >> 1
    # 交换
    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]

    # 插入
    def insert(self,data):
        self.heap.append(data)
        index = len(self.heap) - 1
        parent = self.get_parent_index(index)
        while self.heap[parent] < self.heap[index]and parent >= 0:
            self.swap(index,parent)
            index = parent
            parent = self.get_parent_index(index)

    # 删除堆顶
    def remove(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return temp

    def heapify(self,index):
        total_index = len(self.heap) - 1
        while True:
            max_index = index
            if index * 2 + 1 <= total_index and self.heap[index * 2 + 1] > self.heap[max_index]:
                max_index = index * 2 + 1
            if index * 2 + 2 <= total_index and self.heap[index * 2 + 2] > self.heap[max_index]:
                max_index = index * 2 + 2
            if max_index == index:
                break
            self.swap(index,max_index)
            index = max_index

if __name__ == '__main__':
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(8)
    heap.insert(4)
    heap.insert(3)
    heap.insert(6)
    heap.insert(9)
    print(heap.heap)
    heap.remove()
    print(heap.heap)


