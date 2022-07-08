class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_arr = [0] * len(nums)
        
        count = 0
        oddIndex = 0
        while count <= n-1:
            new_arr[oddIndex] = nums[count]
            oddIndex+= 2
            count += 1
            
        difference = len(nums) - count
        i = 1
        evenIndex = 1
        
        while count <= len(nums):
            new_arr[evenIndex] = nums[count]
            count += 1
            evenIndex += 2
            if i == difference:
                break
            i+=1
            
        return new_arr
