'''24 两两交换链表中的节点'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head is None: return None
        # 设置一个dummy头结点
        if head and head.next is None: return head
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = a
        return dummy.next