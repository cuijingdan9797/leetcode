'''
剑指 Offer 55 - II. 平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归计算树的深度
        def treeDepth(root):
            if not root:
                return 0
            left = treeDepth(root.left)
            right = treeDepth(root.right)
            return 1+ max(left, right)
        # 求左右子树高度差
        if root is None: return True
        left_depth = treeDepth(root.left)
        right_depth = treeDepth(root.right)
        if abs(left_depth-right_depth)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)