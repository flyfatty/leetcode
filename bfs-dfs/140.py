# @Time : 2020/11/1 21:21
# @Author : LiuBin
# @File : 140.py
# @Description : 
# @Software: PyCharm
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        visit = {}

        def dfs(i):
            if i in visit:
                return visit[i]
            if i == len(s):
                return []
            res = []
            flag = False
            for word in wordDict:
                if s[i:].startswith(word):
                    items = dfs(i + len(word))
                    if items == -1:
                        continue
                    flag = True
                    if items:
                        res.extend([word + "" + item for item in items])
                    else:
                        res.append(word)
            visit[i] = res
            return res if flag else -1

        return dfs(0)


print(Solution().wordBreak("abcd", ["a", "abc", "b", "cd"]))
