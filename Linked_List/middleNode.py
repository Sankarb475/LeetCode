#https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

====================================================================================================
#It prints linked list from the middle element 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode """
        
        l=[]
        l1=[]
        if head is None:
            return
        while head is not None:
            current=head
            l.append(current.val)
            head=head.next
        mid=len(l)/2
        l1=l[mid:]
        
        cur = dummy = ListNode(0)
        for e in l1:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
    
        
