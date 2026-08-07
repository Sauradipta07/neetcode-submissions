class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        final = []

        for i in range(n - 2):

            # 1. Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                curr = nums[left] + nums[right]

                if curr < target:
                    left += 1
                elif curr > target:
                    right -= 1
                else:
                    # Found a triplet
                    final.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # 2. Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # 3. Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return final