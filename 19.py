# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        #f = ListNode()
        print(head)
        #print(head.val)
        print(head.next)

        count = 0
        

        while head.next is not None:
            arr.append(head.val)
            count += 1
            head = head.next  # Move to the next node
            #print(head)

        print(arr)
        l = len(arr)+1
        print(l)
        n1 = l-n
        n2 = 0
        n3 = n1
        
        #while n3 != 0:
        #for x in range(l)
             # Move to the next node
        head2 = head

        while head.next is not None:
            if n2==n1:
                #f.append(current.val)
                head == head.next.next

                pass
            n2 = n2+1
            #n3 = n3-1
            head = head.next 



        return head

