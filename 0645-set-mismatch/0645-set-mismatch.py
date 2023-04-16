class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ind = 0
        ans = []
        while ind < len(nums):
            val = nums[ind]-1
            if val != ind:
                if nums[val] != nums[ind]:
                    nums[val],nums[ind] = nums[ind],nums[val]
                    continue
            ind+=1
        ind = 0
        while ind < len(nums):
            val = nums[ind] -1
            if val != ind:
                ans.append(nums[ind])
                ans.append(ind+1)
                break
            ind +=1
        return ans