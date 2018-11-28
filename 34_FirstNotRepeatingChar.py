#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
34.第一个只出现一次的字符
题目：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1。

思路：遍历字符串，用list.count找出只出现一次的字符，结束。
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        for i in range(len(s)):
            c = s.count(s[i])
            if c == 1:
                return i
            else:
                continue
        return -1


if __name__ == '__main__':
    f = Solution()
    r = f.FirstNotRepeatingChar('aabbcds')
    print(r)

