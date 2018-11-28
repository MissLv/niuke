#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
29.最小的K个数
题目：输入n个整数，找出其中最小的K个数，例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        res = sorted(tinput)
        return res[:k]
if __name__ == '__main__':
    tinput = [4,5,1,6,2,7,3,8]
    f = Solution()
    r = f.GetLeastNumbers_Solution(tinput,19)
    print(r)
