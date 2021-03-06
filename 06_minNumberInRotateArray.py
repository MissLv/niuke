#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
6.旋转数组的最小数字
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

题解：二分查找。

'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        _len = len(rotateArray)
        left = 0
        right = _len - 1
        while left <= right:
            mid = int((left + right) >> 1)
            if rotateArray[mid]<rotateArray[mid-1]:
                return rotateArray[mid]
            if rotateArray[mid] >= rotateArray[right]:
                # 说明在【mid，right】之间
                left = mid + 1
            else:
                # 说明在【left，mid】之间
                right = mid - 1
        return rotateArray[mid]

if __name__=='__main__':
    solution = Solution()
    rotateArray = [3,4,5,1,2]
    ans = solution.minNumberInRotateArray(rotateArray)
    print(ans)


