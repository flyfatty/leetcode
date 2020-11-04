# @Time : 2020/11/2 16:22
# @Author : LiuBin
# @File : 15.py
# @Description : 
# @Software: PyCharm
"""三数之和
关键字: 双指针 O(n^2)
思路:
1、分组--正数、负数
2、满足条件的三种情况:
    ① 0,0,0
    ② - target +
    ③ - - + / - + +
"""
from typing import List


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, m = [], {}
        pos, neg = set(), set()
        for i in nums:
            m[i] = m[i] + 1 if i in m else 1
            pos.add(i) if i > 0 else neg.add(i)

        if 0 in m and m[0] >= 3: ans.append((0, 0, 0))
        for p in pos:
            for n in neg:
                target = -(p + n)
                if target in m and (n < target < p or target in (p, n) and m[target] > 1):
                    ans.append((n, target, p))
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
