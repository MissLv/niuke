#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
32.把数组排成最小的数
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

思路：将数组转换成字符串之后，进行两两比较字符串的大小，比如3,32的大小由332和323确定，即3+32和32+3确定。

'''


# class Solution:
#     def PrintMinNumber(self, numbers):
#         if not numbers:
#             return
#         numbers_str = [str(i) for i in numbers]

# class Solution:
#     def cmp(self, a, b):
#         '''定义比较函数'''
#         ab = int(a+b)
#         ba = int(b+a)
#         return 1 if ab > ba else -1
#
#     def PrintMinNumber(self, numbers):
#         string = [str(num) for num in numbers]
#         string.sort(self.cmp, reverse=True)
#         return ''.join(string)
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# class Solution:
#     def cmp(self, a, b):
#         ab = int(a+b)
#         ba = int(b+a)
#         return 1 if ab > ba else -1
#     def PrintMinNumber(self, numbers):
#         return "".join(map(str,sorted(numbers, cmp = lambda a, b : self.cmp(str(a) + str(b), str(b) + str(a)))))
# -*- coding:utf-8 -*-
# class Solution:
#     def PrintMinNumber(self, numbers):
#         # write code here
#         if not numbers:
#             return ""
#         num = map(str, numbers)
#         for i in range(0,len(numbers)):
#             for j in range(i,len(numbers)):
#                 if int(str(numbers[i])+str(numbers[j]))>int(str(numbers[j])+str(numbers[i])):
#                     numbers[i],numbers[j]=numbers[j],numbers[i]
#         ans=''
#         for i in range(0,len(numbers)):
#             ans=ans+str(numbers[i])
#         return ans

from functools import cmp_to_key
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ''
        list1 = sorted(numbers, key=cmp_to_key(self.cmp))

        result = ''.join([str(i)for i in list1])
        return result

    def cmp(self, a, b):
        a1 = str(a)+str(b)
        b1 = str(b)+str(a)
        if a1 < b1:
            return -1
        elif a1 == b1:
            return 0
        else:
            return 1

if __name__=='__main__':
    numbers=[3,32,321]
    solution=Solution()
    ans=solution.PrintMinNumber(numbers)
    print(ans)


# if __name__ == '__main__':
#     f = Solution()
#     r = f.PrintMinNumber([123,321,3])
#     print(r)
