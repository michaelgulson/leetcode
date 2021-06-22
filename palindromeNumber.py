class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = []
        y = str(x)
        for z in y:
            l.append(int(z))
        for w,x in zip(l, reversed(l)):
            if w != x:
                return False
        return True
            
            