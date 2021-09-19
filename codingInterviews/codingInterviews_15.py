'''
剑指 Offer 15. 二进制中1的个数

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

示例 1：

输入：n = 11 (控制台输入 00000000000000000000000000001011)
输出：3
解释：输入的二进制串 00000000000000000000000000001011中，共有三位为 '1'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        # n的最后一位1对应的n-1的位置上一定是0
        # 每次n&(n-1)就会将n中最后一位1变成0，对其他的1没有影响
        sum = 0
        while n!=0:
            n = n&(n-1)
            sum += 1
        return sum