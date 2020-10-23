class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
def isHuan(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            break
                # if slow == fast:
                #     return slow
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n1.next =n2
n2.next =n3
n3.next =n4
n4.next =n5
n5.next =n6
n6.next =n3
print(isHuan(n1))