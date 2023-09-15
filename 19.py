# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        f = ListNode()
    
        #count = 0
        #head3 = head
        nar = str(head).split("next:")
        l = len(nar)-1
        #print(l)
        n1 = l-n
        n2 = 0
        n3 = n1
        
        #while n3 != 0:
        #for x in range(l)
             # Move to the next node
        #head2 = head
        head2 = []

        #while head.next is not None:
        #    if n2==n1:
         #       #f.append(current.val)
          #      head.next == head.next.next
#
 #               pass
  #          n2 = n2+1
   #         #n3 = n3-1
    #        head = head.next 
     #       print(head)
        #for x in range(l):
        #if head.next is None:
            #head2.append(head.val)
        #else:
        while head:
            if n2 == n1:
                print(head)
                n2 = n2+1
                head = head.next

            else:
                head2.append(head.val)
                print(head)
                n2 = n2+1
                head = head.next
                

        print(head2)

