'''
剑指offer 26
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # A和B根节点重合时，判断A是否包含B的结构
        def isSame(t1, t2):
            if t2 is None: return True
            if t1 is None: return False
            if t1.val != t2.val: return False
            return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
        if A is None or B is None: return False
        if isSame(A, B): return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
