# @Time : 2020/10/29 11:45
# @Author : LiuBin
# @File : 1373.py
# @Description : 
# @Software: PyCharm

"""二叉搜索子树的最大键值和

"""
from utils import TreeNode


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs( root ):
            if not root:
                return