"""最长回文子序列
关键字:  DP /  DFS
思路1: 倒序+最长公共子序列
思路2: 最长公共子序列的DFS思路
思路3: 优化成三角DP
"""
class Solution:
    def longestPalindromeSubseq1(self, s: str) -> int:
        def lcs( s1 , s2 ):
            l1 , l2 = len(s1) , len(s2)
            dp = [0] * (l2 + 1)
            for i in range(1,l1+1):
                dp2 = [0] 
                for j in range(1,l2+1):
                    dp2.append( dp[j-1]+1 if s1[i-1]==s2[j-1] else max(dp[j],dp2[-1])) 
                dp = dp2
            return dp[l2]
        return lcs( s , s[::-1])


    def longestPalindromeSubseqByDFS(self, s: str) -> int:
        visit = {}
        def dfs( i , j  ):
            if (i,j) in visit:
                return visit[(i,j)]
            if i == j:
                return 1
            if i > j :
                return 0
            if s[i] == s[j]:
                ret = dfs( i+1 , j-1  ) + 2
            else:
                ret = max( dfs(i+1,j) , dfs(i,j-1)  )
            visit[(i,j)] = ret
            return ret
        return dfs( 0, len(s)-1 )
