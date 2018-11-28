#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
43.左旋转字符串和为S的两个数字
题目：汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
输出描述：对应每个测试案例，输出两个数，小的先输出。


'''

class Solution:
    def LeftRotateString(self, s, n):
        res = s[n:]+s[:n]
        return res




if __name__ == '__main__':

    data = 'abcXYZdef'
    f = Solution()
    r = f.LeftRotateString(data,3)
    print(r)