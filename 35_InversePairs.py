#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
35.数组中的逆序对
题目描述：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007。

输入描述：题目保证输入的数组中没有的相同的数字。

数据范围：
对于%50的数据,size<=10^4
对于%75的数据,size<=10^5
对于%100的数据,size<=2*10^5

示例1
    输入 1,2,3,4,5,6,7,0
    输出 7

'''


import time

# class Solution:
#     def InversePairs(self, data):
#         p = 0
#         for i in range(len(data)):
#             maxs = list(filter(lambda x : x > data[i],data[:i]))
#             p += len(maxs)
#         return p%1000000007

count = 0


class Solution:
    def InversePairs(self, data):
        global count

        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int(len(lists) / 2)
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            print('left: ', left)

            print('right: ', right)

            r, l = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left) - l
                    print('count: ', count)

            result += right[r:]
            result += left[l:]

            return result

        MergeSort(data)
        return count % 1000000007


# 方法二：
class Solution1:
    def InversePairs(self, data):
        # write code here
        start_time = time.clock()
        if data == []:
            end_time = time.clock()
            return 0, end_time - start_time
        else:
            num = 0
            while len(data) > 1:
                num += data.index(min(data))
                data.pop(data.index(min(data)))
            end_time = time.clock()
            return num % 1000000007


if __name__ == '__main__':

    f = Solution()
    r = f.InversePairs([1,2,3,4,5,6,7,0])
    print(r)


