#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
10.矩形覆盖
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
题解：2*1：1种，2*2：2种，2*3：3种，2*4：5种------>斐波那契数列
'''
class Solution:
    # 递归
    def Fibonacci_1(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return n
        return self.Fibonacci_1(n-1)+self.Fibonacci_1(n-2)

    # 非递归
    def Fibonacci_2(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b


if __name__ == '__main__':
    op = Solution()
    res = op.Fibonacci_1(5)
    print(res)