#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1.二维数组中的查找
题目： 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路： 数组array[i+1][j+1],从左下角或者右上角元素开始查找.
      从array[0][j]开始查找，若array[0][j]<val，则j+1,若array[0][j]>val，则j-1
      从array[i][0]开始查找，若array[i][0]<val，则j+1,若array[i][0]>val，则i-1
'''

class Solution:
    # array 二维列表
    def find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        i = 0
        j = len(array[0])-1
        while(i < len(array) and j >= 0):
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


if __name__ == '__main__':
    target = 10
    array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
    solution = Solution()
    res = solution.find(target, array)
    print(res)
