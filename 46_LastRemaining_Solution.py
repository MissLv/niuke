#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
46.孩子们的游戏(圆圈中最后剩下的数)
题目：每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。
    然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
    从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
    请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
题解：约瑟夫环问题
    约瑟夫环（约瑟夫问题）是一个数学的应用问题：已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为k的人开始报数，数到m的那个人出列；
    他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。
    通常解决这类问题时我们把编号从0~n-1，最后 [1]  结果+1即为原问题的解。

'''

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1
        kid = [i for i in range(n)]
        while len(kid)>1:
            index = (m-1)%len(kid)
            kid = kid[index+1:]+kid[:index]
        return kid[0]

    def LastRemaining_Solution2(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        t = 0
        for i in range(2, n + 1):
            t = (t + m) % i
        return t

    def LastRemaining_Solution3(self,n, m):
        list1 = [i for i in range(0, n)]
        t = 0
        for i in range(n - 1):
            t = (t + m - 1) % len(list1)
            list1.pop(t)
        return list1[0]

if __name__ == '__main__':
    f = Solution()
    r = f.LastRemaining_Solution2(5,3)
    print(r)