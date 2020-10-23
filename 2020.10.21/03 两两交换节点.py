class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)
def tworeverse(head):
    dummy = Node(0)
    dummy.next = head
    pre = dummy

    while pre.next and pre.next.next:
        cur = pre.next
        temp = cur.next

        cur.next = temp.next
        temp.next = cur
        pre.next = temp

        pre = pre.next.next

    return dummy.next
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None
print(tworeverse(n1))

