'''
剑指 Offer 39. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。


示例1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票
        # 遇到相同值+1，不同-1，等于0时之前的数都扔掉
        if len(nums)==0: return None
        count = 0
        result = None
        for num in nums:
            if count==0:
                result = num
            if result != num:
                count -=1
            else:
                count +=1
        total = 0
        # 检查这个数是否在数组中出现超过半数
        for num in nums:
            if num == result:
                total += 1
            if total > (len(nums)//2):
                return result
        return 0