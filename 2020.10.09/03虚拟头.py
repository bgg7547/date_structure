#            作用：不用去管链表头   真表头 = 虚拟头.next

# 应用1 链表删除特定值
# 应用 2  lq t24 链表相邻元素交换
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return f"Node({self.data})"
#

#
# def swapPairs(head :Node):
#     dummy = Node(None)
#     dummy.next = head
#     pre = dummy
#     while pre.next and pre.next.next:
#         #指针指向对应位置
#         slow = pre.next
#         fast = pre.next.next
#         #交换位置
#         pre.next = fast
#         slow.next = fast.next
#         fast.next = slow
#         #交换完成，开始下一组
#         pre = pre.next.next
#     return dummy.next

# 应用3 lq T21 合并两个有序链表
  #  用一个空链表 一直往后插入链表中比较小的节点

# def mergeTwoLists( l1, l2):
#     dummy = Node(None)
#     cur = dummy
#     while l1 and l2:
#         if l1.val < l2.val:
#             cur.next = l1
#             l1 = l1.next
#         else:
#             cur.next = l2
#             l2 = l2.next
#         cur = cur.next
#     if l1 is None:
#         cur.next = l2
#
#         if l2 is None:
#             cur.next = l1
#
#         return dummy.next
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None









