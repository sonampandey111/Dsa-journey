class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        ls=0  
        for i,x in enumerate(nums):
            if ls == total-ls-x:
               return i
            ls+=x   
        return -1       



        