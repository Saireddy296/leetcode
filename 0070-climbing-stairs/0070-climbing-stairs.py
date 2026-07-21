class Solution(object):
    def climbStairs(self, n):
        s1=0
        s2=1
        for i in range(n):
            s1,s2=s2,s1+s2
        return s2

        