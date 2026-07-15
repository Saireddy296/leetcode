class Solution(object):
    def addDigits(self, num):
        while(num>=10):
            store=0
            while(num>0):
                d=num%10
                store+=d
                num//=10
            num=store
        return num

        