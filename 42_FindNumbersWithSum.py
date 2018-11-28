#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
42.和为S的两个数字
题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述：对应每个测试案例，输出两个数，小的先输出。

思路：利用i和j从后面进行扫描结果，选取最小的乘积放入到结果集之中。

'''

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        res = []
        for i in data:
            j = tsum-i
            if j in data:
                multiply = i*j
                if res == []:
                    res = [i,j]
                else:
                    if multiply<res[0]*res[1]:
                        res = [i,j]
        return res




if __name__ == '__main__':

    data = [1,2,3,4,5,6,7,8,9]
    f = Solution()
    r = f.FindNumbersWithSum(data,10)
    print(r)