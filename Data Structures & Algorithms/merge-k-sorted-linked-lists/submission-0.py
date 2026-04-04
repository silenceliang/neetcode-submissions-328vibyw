# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2list(list1, list2):
            res = cur = ListNode()
            while list1 and list2:
                if list1.val > list2.val:
                    cur.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next
                cur = cur.next
            if list1:
                cur.next = list1
            if list2:
                cur.next = list2

            return res.next
        
        N = len(lists)
        offset = 1
        while offset < len(lists):
            for i in range(0, len(lists)-offset, 2*offset):
                lists[i] = merge2list(lists[i], lists[i+offset])
            offset*=2
        if lists:
            return lists[0]
        return None