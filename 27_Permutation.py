#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
27.字符串的排列
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入：输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

思路：通过将第k位的字符提取到最前面，然后进行和后面的每个字符进行交换，得到所有结果集。

'''
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = []
        self.helper(ss,res,'')
        return sorted(list(set(res)))

    def helper(self,ss,res,path):
        if not ss:
            res.append(path)
        else:
            for i in range(0,len(ss)):
                print('ss[:i]=',ss[:i],'ss[i+1:]=',ss[i+1:],'res=',res,'path',path+ss[i])
                self.helper(ss[:i]+ss[i+1:],res,path+ss[i])

class Solution2:
    def Permutation(self, ss):
        res = []
        if len(ss) < 2:
            return ss.split()
        for i in range(len(ss)):
            for n in map(lambda x: x+ ss[i], self.Permutation(ss[:i]+ss[i+1:])):
                if n not in res:
                    res.append(n)
        return sorted(res)

if __name__=='__main__':
    str='abbcDe'
    str1='abc'
    solution=Solution()
    ans=solution.Permutation(str1)
    print(ans)

