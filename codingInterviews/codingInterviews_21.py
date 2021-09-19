'''
剑指offer 21 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums =[1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
'''

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums)==0: return []
        # 双指针。前指针过滤所有奇数，遇到偶数时停止不动； 后指针过滤所有偶数，遇到奇数时停止不动
        # 两个指针都不动时，交换两指针所指，各自移动指针
        left = 0
        right = len(nums)-1
        while left<right:
            while left<=len(nums)-1 and nums[left]%2==1:
                left += 1
            while right>=0 and nums[right]%2==0:
                right -= 1
            if left<right:
                if nums[left]%2==0 and nums[right]%2==1:
                    nums[right], nums[left] = nums[left], nums[right]
                    left +=1
                    right -=1
        return nums