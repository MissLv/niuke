#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
5.用两个栈实现队列
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

题解：申请两个栈Stack1和Stack2，Stack1当作输入，Stack2当作pop。当Stack2空的时候，将Stack1进行反转，并且输入到Stack2。
'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2):
            return self.stack2.pop()
        while (self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__=='__main__':
    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    print(solution.pop())
    print(solution.pop())
    print(solution.pop())

eval('1+2')
