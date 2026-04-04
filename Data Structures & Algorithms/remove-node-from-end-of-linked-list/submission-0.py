# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        cur = head
        while cur:
            total+=1
            cur = cur.next
        
        idx = total-n
        if idx == 0:
            return head.next
        cur = head
        c = 0
        while cur:
            if c==idx-1:
                cur.next = cur.next.next
                break
            cur = cur.next
            c+=1
        return head