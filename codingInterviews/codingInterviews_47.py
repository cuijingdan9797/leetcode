'''
剑指offer 47 礼物的最大价值

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
输入:
[
[1,3,1],
[1,5,1],
[4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
'''


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0: return None   # 边界条件
        m = len(grid)   # 矩阵长
        n = len(grid[0])   # 矩阵宽
        dp = [[0*0 for _ in range(n)] for _ in range(m)]   # 初始化
        for i in range(m):
            for j in range(n):
                if i-1 >=0:   # 说明不是第一行
                    lastRow = dp[i-1][j]
                else:   # 当前在第一行
                    lastRow = dp[0][j]
                if j-1 >=0:   # 当前不在第一列
                    lastCol = dp[i][j-1]
                else:   # 当前在第一列
                    lastCol = dp[i][0]
                dp[i][j] = max(lastCol, lastRow) + grid[i][j]
        return dp[m-1][n-1]