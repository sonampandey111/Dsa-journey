class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_counts = {0: 1}

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k

            if remainder in remainder_counts:
                count += remainder_counts[remainder]
                remainder_counts[remainder] += 1
            else:
                remainder_counts[remainder] = 1

        return count
        