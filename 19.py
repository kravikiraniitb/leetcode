class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListNode:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class Solution:

    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def length(h):
            count = 0
            current = h.head  # Start at the head node

            while current is not None:
                count += 1
                current = current.next  # Move to the next node

            return count



        newl = ListNode()
        n2 = length(head) - n
        n3 = 0
        for x in head:

            if n3 != n2:
                newl.append(x)
            n3 = n3+1
        return newl