'''
剑指 Offer 65. 不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
输入: a = 1, b = 1
输出: 2

提示：
a,b均可能是负数或 0
结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
'''


class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 不用加减法就想到 & ^
        # 0^0=1, 0^1=1, 1^1=0 利用这个性质可以找到不进位的
        # &只有两个数都为1才等于1，否则等于0
        # 将加法拆分成两步：第一步统计不考虑进位时候的数是什么，第二步只考虑进位的时候数是什么，最后把他们相加
        # 重复这个操作直到只考虑进位的数等于0，说明结束
        # python需要补码
        a &= 0xffffffff
        b &= 0xffffffff
        while b !=0:
            sum1 = a^b
            b = (a&b)<<1 & 0xffffffff
            a = sum1
        return a if a <= 0x7fffffff else ~(a ^ 0xffffffff)   # #如果是正数的话直接返回 是负数的话,转化成其原码