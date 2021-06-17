#leetcode container with most water problem 11

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        maxVolume = 0
        while i!=j:
            if(height[i]>height[j]):
                volume = (j - i) * height[j]
                if(maxVolume < volume):
                    maxVolume = volume
                j -= 1
            else:
                volume = (j-i) * height[i]
                if(maxVolume < volume):
                    maxVolume = volume
                i += 1
        return maxVolume   