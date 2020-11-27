
"""组合总和IV
关键字: dfs+记忆、DP
思路: dp[t] = sum(dp[t-num[i]]) i<-(0,n)
"""
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]
        for i in range(1 , target+1):
            dp.append(sum([ dp[i - num] for num in nums if i - num >= 0 ]))
        return dp[target]
    
    def combinationSum4ByDFS(self, nums: List[int], target: int) -> int:
        visit = {0:1}
        def dfs( target ):
            if target in visit:
                return visit[target]
            s = 0 
            for num in nums:
                if target - num >= 0 :
                    s += dfs( target - num )
            visit[target] = s
            return s
        return dfs( target )


print(Solution().combinationSum4([1,2,4],32))


