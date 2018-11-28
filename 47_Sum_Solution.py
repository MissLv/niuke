#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
47.求1+2+3+…+n
题目：求1+2+3+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

思路：逻辑短路特性

'''

# class Solution:
#     def Sum_Solution(self, n):
#         if n == 1:
#             return 1
#         return n+self.Sum_Solution(n-1)

class Solution2:
    def Sum_Solution(self, n):
        return n and (n + self.Sum_Solution(n - 1))

if __name__ == '__main__':
    f = Solution2()
    r = f.Sum_Solution(5)
    print(r)