#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
15.反转链表
题目：输入一个链表，反转链表后，输出新链表的表头。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList_1(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pre=None
        while pHead:
            #暂存当前节点的下一个节点信息
            temp = pHead.next
            # 反转节点
            pHead.next = pre
            # 进行下一个节点
            pre = pHead
            pHead = temp
        return pre
    def ReverseList_2(self, pHead):
        head = None
        while (pHead):
            tmp = ListNode(pHead.val)
            tmp.next = head
            head = tmp
            pHead = pHead.next
        return head

    def ReverseList_3(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        p = self.ReverseList_3(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return p

if __name__ == '__main__':
    solution = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p1.next = p2
    p2.next = p3
    ans = solution.ReverseList_3(p1)
    print(ans.val)

