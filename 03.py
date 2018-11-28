#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
3.从尾到头打印链表
题目：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

思路：将链表中的值记录到list之中，然后进行翻转list。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ret = []
        head = listNode
        while (head):
            ret.append(head.val)
            head = head.next
        ret.reverse()
        return ret


if __name__ == '__main__':
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    A5 = ListNode(5)

    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5

    solution = Solution()
    ans = solution.printListFromTailToHead(A1)
    print(ans)
