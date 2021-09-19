'''
剑指offer 40 最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
'''
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 最大堆
        # python没有最大堆只有最小堆
        # 因此要实现最大堆，可以将所有数取反
        # 只有在相反数>堆顶最小（原本数<列表最大）替换堆顶
        if k is None or k==0: return []
        if len(arr)==0 or arr is None: return []
        heap_list = [-x for x in arr[:k]]
        heapq.heapify(heap_list)
        for elem in arr[k:]:
            if -elem > heap_list[0]:
                heapq.heappop(heap_list)
                heapq.heappush(heap_list, -elem)
        return [-x for x in heap_list]
