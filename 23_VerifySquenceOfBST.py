#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
23.二叉树的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：二叉搜索树的特性是所有左子树值都小于中节点，所有右子树的值都大于中节点，递归遍历左子树和右子树的值。
    1、确定root；
    2、遍历序列（除去root结点），找到第一个大于root的位置，则该位置左边为左子树，右边为右子树；
    3、遍历右子树，若发现有小于root的值，则直接返回false；
    4、分别判断左子树和右子树是否仍是二叉搜索树（即递归步骤1、2、3）

'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        size = len(sequence)
        if size == 0:
            return False
        size -= 1
        index = 0
        while size:
            while index < size and sequence[index] < sequence[size]:
                index += 1
            while index < size and sequence[index] > sequence[size]:
                index += 1
            if index < size:
                return False
            index = 0
            size -= 1
        return True

    def VerifySquenceOfBST2(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        root = sequence[-1]

        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1

        for node in sequence[i:-1]:
            if node < root:
                return False
        left = True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])

        right = True
        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i+1:-1])
        return left and right
if __name__=='__main__':
    solution = Solution()
    data = [1, 5, 4, 3, 2, 1, 2, 8]
    ans = solution.VerifySquenceOfBST2(data)
    print(ans)
