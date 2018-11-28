#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
14.链表中倒数第K个节点
题目：输入一个链表，输出该链表中倒数第k个结点。

题解：两个指针p,q p先走k步。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        #反转链表
        p1 = p2 = head
        for i in range(k):
            if p1 == None:
                return None
            p1 = p1.next
        while (p1):
            p2 = p2.next
            p1 = p1.next
        return p2
if __name__=='__main__':
    solution=Solution()
    k=3
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p4=ListNode(4)
    p1.next=p2
    p2.next=p3
    p3.next=p4

    ans=solution.FindKthToTail(p1,k)
    print(ans.val)
