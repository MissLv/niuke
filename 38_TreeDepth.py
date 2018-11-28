#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
37.二叉树的深度
题目：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, root):

        if root == None:
            return 0
        # print(root.val)
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        # print('----',left,right)
        return max(left,right)+1
if __name__ == '__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A4.left = A6

    solution = Solution()
    ans = solution.TreeDepth(A1)
    print('ans=', ans)
