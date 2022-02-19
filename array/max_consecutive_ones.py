class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # initialize maximum
        result = 0
        # initialize count
        count = 0
        
        for i in range(0,len(nums)):
            # reset count to 0
            if nums[i] == 0:
                count = 0
            # check maximum count and save
            if count > result:
                result = count
                
            count += 1
            
        return result
