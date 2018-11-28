#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
2.替换空格
题目： 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

思路：利用字符串中的replace直接替换即可
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        temp = s.replace(" ", "%20")
        return temp

if __name__=='__main__':
    s = 'We Are Happy'
    solution = Solution()
    ans = solution.replaceSpace(s)
    print(ans)

