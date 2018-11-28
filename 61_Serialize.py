#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
61.序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树。

思路：转变成前序遍历，空元素利用”#”代替，然后进行解序列。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None
        root = None

        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

if __name__=="__main__":
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    A3.left=A6
    A3.right=A7

    solution = Solution()
    ans=solution.Serialize(A1)
    print(ans)
    root=solution.Deserialize(ans)
    res=solution.Serialize(root)
    print(res)
