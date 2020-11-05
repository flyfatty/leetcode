# @Time : 2020/11/4 22:22
# @Author : LiuBin
# @File : 322.py
# @Description : 
# @Software: PyCharm

"""零钱兑换
思路
1、最少数量，想到BFS,但是会超时
2、记忆化搜索: 利用DFS缩小问题规模,返回每个规模的最少硬币数
3、DP: dp[i] = min(dp[t-i] + 1 , dp[i])
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for i in range(1, amount + 1):
            dp.append(float('inf'))
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChangeByDFS(self, coins: List[int], amount: int) -> int:
        visit = {}

        def dfs(amount):
            if amount in visit:
                return visit[amount]
            if amount == 0: return 0
            if amount < 0: return -1
            res = float('inf')
            for coin in coins:
                sub_res = dfs(amount - coin)
                if sub_res == -1: continue
                res = min(res, sub_res + 1)
            visit[amount] = -1 if res == float('inf') else res
            return visit[amount]

        return dfs(amount)

    def coinChangeByBFS(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        q = [amount - coin for coin in coins if amount - coin >= 0]
        step = 1
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.pop(0)
                if cur == 0: return step
                for coin in coins:
                    if cur - coin >= 0:
                        q.append(cur - coin)
            step += 1
        return -1


print(Solution().coinChange(coins=[2], amount=3))
