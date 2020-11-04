# @Time : 2020/10/21 16:21
# @Author : LiuBin
# @File : 10.py
# @Description : 
# @Software: PyCharm
"""正则表达式
关键字: 回溯
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        flag = False
        if s == p == "":
            return True
        if len(p) > 1 and p[1] == "*":
            flag = self.isMatch(s, p[2:])
            if flag: return flag
            i = 0
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                while i < len(s) and (i == 0 or s[i - 1] == s[i] or p[0] == '.'):
                    flag = self.isMatch(s[i + 1:], p[2:])
                    if flag: break
                    i += 1
        elif len(s) > 0 and len(p) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        return flag


print(Solution().isMatch("aa", "a*"))
