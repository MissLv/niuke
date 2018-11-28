#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
9.变态跳台阶
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
题解：ans[n]=ans[n-1]+ans[n-2]+ans[n-3]+…+ans[n-n]，ans[n-1]=ans[n-2]+ans[n-3]+…+ans[n-n]，ans[n]=2*ans[n-1]
'''

class Solution:
    def jump(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return 2*self.jump(n-1)
if __name__ == '__main__':
    op = Solution()
    res = op.jump(2)
    print(res)