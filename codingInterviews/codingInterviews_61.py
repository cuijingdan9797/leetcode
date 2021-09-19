'''
剑指offer 61 扑克牌中的顺子

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例1:
输入: [1,2,3,4,5]
输出: True

示例2:
输入: [0,0,1,2,5]
输出: True

限制：
数组长度为 5
数组的数取值为 [0, 13] .

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
'''

class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 不能有重复
        # 最大-最小<=4
        no_repeat = set()
        min_num = 14
        max_num = 0
        for elem in nums:
            if elem !=0:
                if elem in no_repeat: return False
                no_repeat.add(elem)
                min_num = min(min_num, elem)
                max_num = max(max_num, elem)
        return max_num-min_num <=4