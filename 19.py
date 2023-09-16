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
                #print(head)
                n2 = n2+1
                head = head.next

            else:
                head2.append(head.val)
                #print(head)
                n2 = n2+1
                head = head.next
                
        head2.reverse()
        def ll(x,y):
            if  x == y:
                # y - index last element
                f = ListNode(head2[x])
                f.next = None
                print(f)
            else:
                f = ListNode(head2[x])
                f.next = ll(x+1,y)
                print(f)


        #def formlinkedlist(x,y):
        #[5,3,2,1]
        #for x in range(len(head2)):
        x = 0
        while x < len(head2):
            y = len(head2)-1
            print(x)
            #print(y)
            if  x == 0:
                # y - index last element
                f = ListNode(head2[x])
                f.next = None
                print(f)
            else:
                f = ListNode(head2[x])
                #f.next = ll(x-1,y)
                f.next = ListNode(head2[x-1])
                print(f)

            x = x+1
            #ll(x,y)
            #if x == 0:
             #   nextt = None
              #  val = head2[x]
               # #f(val,nextt)
                #f = ListNode(val)
              #  f.next = nextt
            #else:
             #   nextt=head2[x-1]
              #  val = head2[x]
               # #f(val,nextt)
               # f = ListNode(val)
              #  f.next = nextt

            
        return f
        #print(head2)

        