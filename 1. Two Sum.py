class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

'''
To solve this efficiently we can use a dictionary that can store both the index and the number as it steps through the set. First initialize an empty dictionary. Instead of building nums as a normal list, we can ennumerate it so that it can carry over its index as well.
As we loop through i we will do the following. Num will return whatever number is associated with the ith index of the array, and since we used enumerate we will not need to increment i. It will then sutract num from target and checkto see if that value is in
seen{}. if not, it will store seen[num] = i which is a fancy way of saying num where index is i. it will then try the next number and attempt to find that complement in seen, if it does not find it, it will add another record into the dictionary and continue.
If it does find it's compliment it will return a list of [seen[compliment], i]. This will work because it will return the index of both the current number and its compliment from seen as an array of 2 nums. Since we only need one answer this works.
'''