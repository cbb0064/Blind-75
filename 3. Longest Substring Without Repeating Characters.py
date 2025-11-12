class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = max_len = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    '''
    This is a sliding window implementation where we anchor a left pointer and move the right until we hit a duplicate. First we initialize the characters as a set. We then define the max length as left and set that all equal to 0
    After this we will start looping through the range of the length of the string, setting the index to the right pointer and do the following. It will check to see if the current string value of my right pointer exists in the char set.
    If it does not, we add the character to the set and compare the current max value to the value of this equation. Right - left + 1. In the case that the string value of right exists in the char set, we will find the string character
    at the index of left, remove it from the set, and increment left by 1. We will add the string value of right to the set. Now, we will now re run this calculation of right-left+1 with this new left value and see if it is greater than the current max length.
    Keep looping through like this and you will have the greatest value for max length
    '''