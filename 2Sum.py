
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        hashTable = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if(compliment in hashTable):
                ret.append(hashTable[compliment])
                ret.append(i)
            else:
                hashTable[nums[i]] = i
                
        return ret