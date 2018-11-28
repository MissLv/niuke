#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
8.跳台阶
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
题解：斐波那契数列 f(n)=f(n-1)+f(n-2)
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
    res = op.Fibonacci_1(10)
    print(res)