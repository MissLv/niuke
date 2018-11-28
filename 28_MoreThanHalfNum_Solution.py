#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
28.数组中出现次数超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0

题解：collections.Counter;list.count;摩尔投票算法。

    Boyer-Moore majority vote algorithm(摩尔投票算法)
    简介：Boyer-Moore majority vote algorithm(摩尔投票算法)是一种在线性时间O(n)和空间复杂度的情况下，在一个元素序列中查找包含最多的元素。
        它是以Robert S.Boyer和J Strother Moore命名的，1981年发明的，是一种典型的流算法(streaming algorithm)。
        在它最简单的形式就是，查找最多的元素，也就是在输入中重复出现超过一半以上(n/2)的元素。
        如果序列中没有最多的元素，算法不能检测到正确结果，将输出其中的一个元素之一。当元素重复的次数比较小的时候，对于流算法不能在小于线性空间的情况下查找频率最高的元素。

    算法描述： 算法在局部变量中定义一个序列元素(m)和一个计数器(i)，初始化的情况下计数器为0.
            算法依次扫描序列中的元素，当处理元素x的时候，如果计数器为0，那么将x赋值给m，然后将计数器(i)设置为1，如果计数器不为0，那么将序列元素m和x比较，如果相等，那么计数器加1，如果不等，那么计数器减1。
            处理之后，最后存储的序列元素(m)，就是这个序列中最多的元素。如果不确定是否存储的元素m是最多的元素，还可以进行第二遍扫描判断是否为最多的元素。
'''

from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        res = Counter(numbers)
        m = res.most_common(1)
        if m[0][1] > int(len(numbers)/2):
            return m[0][0]
        else:
            return 0
    def MoreThanHalfNum_Solution2(self, numbers):
        d = {}
        for i in numbers:
            d[i] = numbers.count(i)
        print(d)
        for k, v in d.items():
            if v > int(len(numbers)/2):
                return k
            else:
                continue
        return 0

    def MoreThanHalfNum_Solution3(self, numbers):
        # write code here
        if numbers == []:
            return 0
        val, cnt = None, 0
        for num in numbers:
            if cnt == 0:
                val, cnt = num, 1
            elif val == num:
                cnt += 1
            else:
                cnt -= 1
        return val if numbers.count(val) * 2 > len(numbers) else 0


if __name__ == '__main__':
    s = [1,2,3,2,4,5,2,2,2]
    f = Solution()
    r = f.MoreThanHalfNum_Solution3(s)
    print(r)
