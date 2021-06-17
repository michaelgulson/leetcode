#Leetcode Problem 15 3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        hashTable = {}     
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                compliment = -1*(nums[i]+nums[j])
                if(i==j):
                    continue
                elif(compliment in hashTable):
                    retList = [nums[i], nums[j], compliment]
                    ret.append(retList)
                    hashTable.pop(compliment)
                    break
                else:
                    hashTable[nums[i]] = nums[i]
        return ret