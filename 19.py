# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        f = ListNode()

        count = 0
        #current = get_first_element(head)  # Start at the head node
        if head.next is not None:
            current = head.val
        else:
            current = None  # The list is empty


        while current is not None:
            arr.append(current)
            count += 1
            current = current.next  # Move to the next node

        
        l = len(arr)
        n1 = l-n
        n2 = 0
        
        while current is not None:
            if n2!=n1:
                f.append(current)
            n2 = n2+1
            count += 1
            current = current.next  # Move to the next node
        return f

