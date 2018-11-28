#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
26.二叉搜索树与双向列表
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

思路：递归将根结点和左子树的最右节点和右子树的最左节点进行连接起来,左子树上最右结点 -> root -> 右子树上的最左结点

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return pRootOfTree
        if pRootOfTree.left == None and pRootOfTree.right == None:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        p = left
        if left:
            while(p.right):
                p = p.right
            p.right = pRootOfTree
            pRootOfTree.left = p
        right = self.Convert(pRootOfTree.right)
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree
        return left if left else pRootOfTree


if __name__=='__main__':
    A1 = TreeNode(7)
    A2 = TreeNode(5)
    A3 = TreeNode(15)
    A4 = TreeNode(2)
    A5 = TreeNode(6)
    A6 = TreeNode(8)
    A7 = TreeNode(19)
    A8 = TreeNode(24)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7
    A7.right = A8

    solution = Solution()
    res = solution.Convert(A1)
    print(res)

