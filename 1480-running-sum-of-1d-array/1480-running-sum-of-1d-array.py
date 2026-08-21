class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        rs=[]
        for i in nums:
            s+=i
            rs.append(s)
        return rs 
        