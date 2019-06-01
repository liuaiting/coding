# coding=utf-8
#Given a singly linked list L: L0→L1→…→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→… 
#
# You may not modify the values in the list's nodes, only nodes itself may be changed. 
#
# Example 1: 
#
# 
#Given 1->2->3->4, reorder it to 1->4->2->3. 
#
# Example 2: 
#
# 
#Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second part
        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        # merge the first and second part
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next
        return
