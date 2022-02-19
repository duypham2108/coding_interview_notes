class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final_nums = [0 for i in nums]
        
        left, right = 0, n-1
        
        
        tracker = n-1
        while tracker >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                final_nums[tracker] = (nums[left]**2)
                left += 1
            else:
                final_nums[tracker] = (nums[right]**2)
                right -= 1
                
            tracker -= 1
        
        return final_nums
        
        
