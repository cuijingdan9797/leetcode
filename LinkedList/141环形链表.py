'''141 环形链表'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针、set都可以求解
        if not head: return None
        low = head
        fast = head
        while fast and low and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                return True
        return False