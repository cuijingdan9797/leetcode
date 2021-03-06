'''
剑指offer 63 股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划：比较（当前价格-历史最低点）和前一天的最大利润
        if len(prices)==0: return 0
        dp = 0   # 最大利润
        minPrice = prices[0] # 历史最低价格
        for i in range(len(prices)):
            if prices[i] > minPrice:
                curPrice = prices[i] - minPrice
                dp = max(dp, curPrice)
            else:
                minPrice = prices[i]
        return dp
