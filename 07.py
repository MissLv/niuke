#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
7.斐波那契数列
题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39。

题解：递归和非递归方法。
'''

class Solution:
    # 递归
    def Fibonacci_1(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.Fibonacci_1(n-1)+self.Fibonacci_1(n-2)

    # 非递归
    def Fibonacci_2(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b


if __name__ == '__main__':
    op = Solution()
    res = op.Fibonacci_2(20)
    print(res)