# Brute Force
class Solution_V1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)
        return None

# dictionary (Hash Table)
class Solution(object):
    def twoSum(self,nums, target):
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = i

        for i in range(len(nums)):
            find_key = target - nums[i]
            if a.keys().__contains__(find_key) and a[find_key] != i:
                return (i, a[find_key])
        raise Exception("NO!")

if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,4,8]
    target = 9
    print solution.twoSum(nums=nums, target=target)
