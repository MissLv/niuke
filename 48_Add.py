#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
48.不用加减乘除做加法
题目：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
思路：逻辑短路特性

'''

class Solution:
    # 加法
    def Add(self, num1, num2):
        return sum([num1,num2])

    def Add2(self, a, b):
        while b:
            a, b = (a ^ b) & 0xffffffff, ((a & b) << 1) & 0xffffffff
        return a if a <= 0x7fffffff else ~(a ^ 0xffffffff)

    # 减法
    def substract(self,a,b):
        mid = self.Add2(~b,1)
        return self.Add2(a,mid)

    # 乘法
    def multiply(self,a,b):
        multiplicand = a if a >= 0 else self.Add2(~a,1)
        multiplier = b if b >= 0 else self.Add2(~b,1)
        product = 0
        count = 0
        while(count<multiplier):
            product = self.Add2(product, multiplicand)
            count = self.Add2(count, 1)
        if (a ^ b) < 0:
            product = self.Add2(~product, 1)
        return product

    def multiply2(self, a, b):
        multiplicand = a if a >= 0 else self.Add2(~a, 1)
        multiplier = b if b >= 0 else self.Add2(~b, 1)
        product = 0
        while multiplier != 0:
            if multiplier & 1:
                product = self.Add2(product, multiplicand)
            multiplicand = multiplicand << 1
            multiplier = multiplier >> 1
            if (a ^ b) < 0:
                product = self.Add2(~product, 1)
        return product





if __name__ == '__main__':
    f = Solution()
    r = f.Add2(0,0)
    print(r)