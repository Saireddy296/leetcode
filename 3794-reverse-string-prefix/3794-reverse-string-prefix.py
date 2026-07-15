class Solution(object):
    def reversePrefix(self, s, k):
        # return s[:k][::-1] + s[k:]
        first=s[:k]
        first=first[::-1]
        second=s[k:]
        return first+second
        
        