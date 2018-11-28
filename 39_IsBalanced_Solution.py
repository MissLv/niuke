#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
39.平衡二叉树
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。

题解：平衡二叉树是左右子数的距离不能大于1，因此递归左右子树，判断子树距离是否大于1。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, root):
        if not root:
            return 0
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        # print('----',left,right)
        return max(left,right)+1

    def is_balance(self, root):
        if root == None:
            return
        return abs(self.TreeDepth(root.left)-self.TreeDepth(root.right)) <= 1


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
    ans = solution.is_balance2(A1)

    print(ans)
