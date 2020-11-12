# @Time : 2020/11/12 12:45
# @Author : LiuBin
# @File : 1143.py
# @Description : 
# @Software: PyCharm
"""
关键字: DP
dp[i][j] 截止到分别i,j位的LCS
dp[i][j] = dp[i-1][j-1] + 1 if a[i] == b[j] else max( dp[i-1][j] , dp[i][j-1] )
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]

    def longestCommonSubsequenceByDFS(self, text1: str, text2: str) -> int:
        visit = {}

        def dfs(i, j):
            if (i, j) in visit:
                return visit[(i, j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            n = dfs(i + 1, j + 1) + 1 if text1[i] == text2[j] else max(dfs(i, j + 1), dfs(i + 1, j))
            visit[(i, j)] = n
            return n

        return dfs(0, 0)


print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
