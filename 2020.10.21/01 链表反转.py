class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)
def reverse(head):

    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre

        pre = cur
        cur = temp

