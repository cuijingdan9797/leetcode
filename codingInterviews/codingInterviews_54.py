'''
剑指offer 54 二叉搜索树的第K大个节点

给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
  2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # ===========方法一==================
        # 二叉搜索树中序遍历
        # 倒数第k大节点
        middle_order = []
        def middle_order_tree(root):
            if root is None: return None
            middle_order_tree(root.left)
            middle_order.append(root.val)
            middle_order_tree(root.right)
        middle_order_tree(root)
        return middle_order[-k]

        # ===============方法二================
        # 先遍历左子树，根，最后右子树
        self.count = k
        k_list = []
        def buildKlist(root):
            if root is None: return None
            buildKlist(root.right)
            if self.count<=0: return
            self.count -= 1
            k_list.append(root.val)
            buildKlist(root.left)
        buildKlist(root)
        return k_list[-1]