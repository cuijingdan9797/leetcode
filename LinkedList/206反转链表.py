'''206. 反转链表'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 需要记录节点的前驱
        prev = None
        cur = head
        while cur:
            nx = cur.next   # 记录节点后继，防止找不到
            cur.next = prev
            prev = cur
            cur = nx
        return prev