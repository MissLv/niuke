#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
12.数值的整次方
题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        ans = exp = pos = 1
        if exponent < 0:
            pos, exponent = -1, -exponent
        while (exponent):
            if exponent % 2:
                ans = ans * (base ** (exp))
            exponent = exponent >> 1
            exp = exp * 2
        return ans if pos == 1 else 1.0 / ans
if __name__=='__main__':
    solution=Solution()
    base=float(2.43)
    exponent=int(5)
    ans=solution.Power(base,exponent)
    print(ans)

