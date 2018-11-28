#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
31.整数中1出现的次数
题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

思路：对每个数字的每位进行分解，含有1则结果加1。

'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        data_list = [str(i) for i in range(1,n+1)]
        data_str = ''.join(data_list)
        return data_str.count('1')
if __name__ == '__main__':
    f = Solution()
    r = f.NumberOf1Between1AndN_Solution(1)
    print(r)