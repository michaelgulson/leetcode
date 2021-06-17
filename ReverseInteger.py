#Leetcode Problem #7 Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        string = string[::-1]
        #print (string)
        ret = int(string)
        return ret