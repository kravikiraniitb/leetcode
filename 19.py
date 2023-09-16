# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        nar = str(head).split("next:")
        l = len(nar)-1
        n1 = l-n
        n2 = 0
        f = ListNode()
        head2 = []

        while head:
            if n2 == n1:
                n2 = n2+1
                head = head.next
            else:
                head2.append(head.val)
                n2 = n2+1
                head = head.next
                
        if len(head2) == 0:
            return None
        
        head2.reverse()
    
        p = None
        x = 0
        while x < len(head2):
            y = len(head2)-1
            if  x == 0:
                f = ListNode(head2[x])
                f.next = None
                nextt = f
            else:
                f = ListNode(head2[x])
                if (bool(p) and bool(nextt)) :
                    f.next = p
                    p = f
                else:
                    f.next = nextt
                    p = f
            x = x+1
        return f
       

        