class Solution(object):
    def reverseByType(self, s):
        l=[c for c in s if c.isalpha()][::-1]
        sp=[c for c in s if not c.isalpha()][::-1]
        ans = ""
        for c in s:
            if c.isalpha():
                ans += l.pop(0)
            else:
                ans += sp.pop(0)
        return ans
        