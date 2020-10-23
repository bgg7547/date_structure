class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __repr__(self):
        return f"Node({self.val})"
class solution:
    def hebin(self,l1,l2):
        dum = Node(None)
        cur = dum
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1
        return dum.next

def hebin(self,l1,l2):
    dum = Node(None)
    cur = dum
    while l1 or l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
        if l1 is None:
            cur.next = l2
            break
        if l2 is None:
            cur.next = l1
            break
    return dum.next

