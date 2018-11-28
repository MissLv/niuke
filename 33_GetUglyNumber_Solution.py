#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
33.丑数
题目：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路：每一个丑数必然是由之前的某个丑数与2，3或5的乘积得到的，这样下一个丑数就用之前的丑数分别乘以2，3，5，找出这三这种最小的并且大于当前最大丑数的值，即为下一个要求的丑数。

'''
import heapq


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if (index <= 0):
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0
        for i in range(index-1):
            newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
            uglyList.append(newUgly)
            if (newUgly % 2 == 0):
                indexTwo += 1
            if (newUgly % 3 == 0):
                indexThree += 1
            if (newUgly % 5 == 0):
                indexFive += 1
        return uglyList

    def GetUglyNumber_Solution2(self, index):
        # write code here
        if index < 1:
            return 0
        heaps = []
        heapq.heappush(heaps, 1)
        lastnum = None
        idx = 1
        while (idx <= index):
            curnum = heapq.heappop(heaps)
            while (curnum == lastnum):
                curnum = heapq.heappop(heaps)
            lastnum = curnum
            idx += 1
            heapq.heappush(heaps, curnum * 2)
            heapq.heappush(heaps, curnum * 3)
            heapq.heappush(heaps, curnum * 5)
        return lastnum[-1]


if __name__=='__main__':
    solution=Solution()
    index=200
    ans=solution.GetUglyNumber_Solution(index)
    print(ans)
