#左右两个区域，左侧是排好的，右侧是乱序的，（扑克）  右侧往左侧插
# 左侧边界是靠右侧right维护的

# def insertSort(nums):
#     for r in range(1,len(nums)):
#         target = nums[r]
#         for l in range(r):
#             if nums[l] > target:
#                 nums[l + 1: r + 1] = nums[l: r]
#                 nums[l] = target
#                 break
#     return nums
# print(insertSort([3,2,4,8,1]))

# 链表
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return("Node({})".format(self.data))

def insertSort_linklist(head):
    dummy = Node(0)  # 创建虚拟节点
    pre = dummy
    cur = head
    while cur:       # 遍历待排序节点
        temp = cur.next
        while pre.next and pre.next.data < cur.data:   # 找到插入位置
            pre = pre.next

        cur.next = pre.next
        pre.next = cur

        cur = temp
        pre = dummy
    return dummy.next
