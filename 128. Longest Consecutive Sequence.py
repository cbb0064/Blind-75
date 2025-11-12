class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
    
'''
To solve this we need to check to first check to see if we have nums. If no nums are passed in then we return 0. If nums are passed in, convert them to a set so the lookups occur in O(1) time complexities.
From here we initialize max_length to 0 which will later be overwritten by the value found with our for loop. Here what we do is for every num in num_set, check to see if a predecessor exists. 
If it does not exist and there is no number one higher in the set, it will set current length to 1 and then compare to the max length. If a predecessor does exist, it will skip the number entirely. 
When it does not have an immediate predecesor and there exists an n+1 number from the current it will do the following. It will first set current length to 1. Then it will loop through each number
procedurally until there are no more sucessors, incrementing current length by 1 every time it finds a new number. After it can no longer find any sucessors (i.e it has finished its run) it will
then compare the current length to the previous highest maximum and if it is larger it will override the old value. Finally, after looping through all numbers in the set, return the final max length.
'''