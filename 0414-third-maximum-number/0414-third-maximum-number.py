class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        if len(distinct_nums) < 3:
            return max(distinct_nums)
        distinct_nums.remove(max(distinct_nums))
        distinct_nums.remove(max(distinct_nums))
        return max(distinct_nums)
        