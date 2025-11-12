class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r += 1
            return r - l - 1

        max_len = 0
        start = 0

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            curr_len = max(len1, len2)

            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start:start + max_len]
    
    '''
    This one is a bit tougher, in order to do this we need to define an expand function that takes in left and right bounds. We create a while loop that checks that the bounds are still within the range of the string. if the bounds are true return r - l - 1.
    After that we can initialize the max length and start values that will be used later. Start will refernce the index of the palindrome to get where to parse from and max length is and int value that represents the longest stored palindrome length.
    We create a for loop that will check on every character as a center value, taking into account double character centers as well. the expand function will continue looping from the center, incrementing l and r by one until the values do not align.
    After passing through each possible center, we will store the length as a max and compare each one against the previous. Finally we will be left with the max length of the palindrome and use this along with start to parse the final string
    '''