#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
51.构建乘积数组
题目:给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
思考：分为下三角和上三角DP计算B
    下三角B[i]=A[0]A[1]A[2]..A[i−1]=B[i−1]A[i−1]B[i]=A[0]A[1]A[2]..A[i−1]=B[i−1]A[i−1]
    上三角（从最后往前）tmp=A[−1]A[−2]A[−3]...

'''

# class Solution:
#     def multiply(self, A):
#         # write code here
#         B=[]
#         for i in range(0,len(A)):
#             temp=1
#             for j in range(0,len(A)):
#                 if j==i:
#                     continue
#                 temp=temp*A[j]
#             B.append(temp)
#         return B
class Solution2:
    def multiply(self, A):
        # write code here
        size = len(A)
        B = [1]*size
        for i in range(1,size):
            B[i] = B[i-1]*A[i-1]
        tmp = 1
        for i in range(size-2,-1,-1):
            tmp = tmp*A[i+1]
            B[i] = B[i]*tmp
        return B

if __name__=='__main__':
    solution=Solution2()
    A=[1,2,3,4,5]
    ans=solution.multiply(A)
    print(ans)
