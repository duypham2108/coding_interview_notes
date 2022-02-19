class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_pivot(nums, low, high):
    
            # check if sorted array
            if high < low:
                return -1
            # check if one element array
            if high == low:
                return low

            mid = int(low + (high - low)/2)

            if mid < high and nums[mid] > nums[mid + 1]:
                return mid
            if mid > low and nums[mid] < nums[mid - 1]:
                return (mid-1)
            if nums[low] >= nums[mid]:
                return find_pivot(nums, low, mid-1)

            return find_pivot(nums, mid+1, high)
        
        def binary_search(nums, left, right, target):
            
            if right < left:
                return -1
            
            pivot = int(left + (right - left)/2)
            if nums[pivot] == target:
                return pivot
            
            if nums[pivot] < target:
                return binary_search(nums, pivot+1, right,target)
            
            return binary_search(nums, left, (pivot-1), target)
        
        pivot = find_pivot(nums, 0, len(nums)-1)
        
        if pivot == -1:
            return binary_search(nums, 0, len(nums)-1, target)
        
        
        if nums[0] <= target:
            return binary_search(nums, 0, pivot-1, target);
        return binary_search(nums, pivot + 1, len(nums)-1, target);
        
        
        
                    
