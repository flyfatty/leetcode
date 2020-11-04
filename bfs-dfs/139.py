# @Time : 2020/11/2 9:17
# @Author : LiuBin
# @File : 139.py
# @Description : 
# @Software: PyCharm
"""单词拆分
关键字: 记忆化递归、DP
思路:
# 状态: dp[i] 截止到i,是否可以拆分
# 状态转移方程:   dp[i] = dp[j] and check(j,i)
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [True]
        for i in range(1, len(s) + 1):
            dp.append(False)
            for j in range(0, i):
                dp[-1] = dp[j] and s[j:i] in wordSet
                if dp[-1]: break
        return dp[-1]

    def wordBreakByDFS(self, s: str, wordDict: List[str]) -> bool:
        visit = {}

        def dfs(i):
            if i in visit:
                return visit[i]
            if i == len(s):
                return True
            flag = False
            for word in wordDict:
                if s[i:].startswith(word):
                    flag = dfs(i + len(word))
                    if flag:
                        break
            visit[i] = flag
            return flag

        return dfs(0)


print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code", "sand", "and", "cat"]))
