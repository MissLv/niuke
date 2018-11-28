#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
17.树的子结构
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构
树的子结构：子结构只要包含任意相连的任意数量的结点即可，意思是包含了一个结点，可以只取左子树或者右子树，或者都不取。
树的子树：子树只要包含了一个结点，就得包含这个结点下的所有节点。因此，A树与其子树一定最后同时访问到空指针。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        def subtree(pRoot1,pRoot2):
            if pRoot2 == None and pRoot1 == None:
                return True
            if pRoot2 == None:
                return False
            if pRoot1 == None:
                return False

            if pRoot2.val == pRoot1.val:
                if pRoot2.left == None and pRoot2.right == None:
                    return True
                if subtree(pRoot1.left,pRoot2.left) and subtree(pRoot1.right,pRoot2.right):
                    return True
            return subtree(pRoot1.left,pRoot2) or subtree(pRoot1.right,pRoot2)
        if pRoot1 == None and pRoot2 == None:
            return False
        return subtree(pRoot1,pRoot2)
if __name__=='__main__':
    solution=Solution()
    pRootA1 = TreeNode(1)
    pRootA2 = TreeNode(2)
    pRootA3 = TreeNode(3)
    pRootA4 = TreeNode(4)
    pRootA5 = TreeNode(5)
    pRootA1.left = pRootA2
    pRootA1.right = pRootA3
    pRootA2.left = pRootA4
    pRootA2.right = pRootA5

    pRootB2 = TreeNode(2)
    # pRootB4 = TreeNode(4)
    # pRootB5 = TreeNode(5)
    # pRootB2.left = pRootB4
    # pRootB2.right = pRootB5
    ans=solution.HasSubtree(pRootA1, pRootB2)
    print(ans)
