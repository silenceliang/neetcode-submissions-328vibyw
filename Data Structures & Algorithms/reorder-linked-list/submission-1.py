# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the median
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow (inclusively) is the last half
        # reverse the last half
        second = slow.next
        slow.next = None

        rev = None
        while second:
            next_node = second.next
            second.next = rev
            rev = second
            second = next_node
        
        # interleave two linkedlists
        first, second = head, rev
        while second:
            t1, t2 = first.next, second.next
            first.next, second.next = second, t1
            first, second = t1, t2
