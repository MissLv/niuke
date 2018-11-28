#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
37.数字在排序数组中出现的次数
题目：统计一个数字在排序数组中出现的次数。
题解：二分查找
'''

import time
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


    def GetNumberOfK2(self, data, k):
        # write code here
        if len(data) == 0:
            return 0
        else:
            count, mid = 0, len(data) // 2
            if k > data[mid]:
                for i in range(mid + 1, len(data)):
                    if data[i] == k:
                        count += 1
                return count
            elif k < data[mid]:
                for i in range(mid - 1, -1, -1):
                    if data[i] == k:
                        count += 1
                return count
            else:
                count += 1
                for i in range(mid - 1, -1, -1):
                    if data[i] == k:
                        count += 1
                    else:
                        break
                for i in range(mid + 1, len(data)):
                    if data[i] == k:
                        count += 1
                    else:
                        break
                return count

if __name__ == '__main__':
    data = [i for i in range(1000)]
    f = Solution()
    r = f.GetNumberOfK2(data,999)
    print(r)
