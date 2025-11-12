class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        result.append(word1[i:])
        result.append(word2[i:])
        return ''.join(result)
'''
You are given two strings word1 and word2. Merge the strings by adding letters in 
alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

To solve this, initialize an array (here it is initialized as a result). Since we are looping through each word, we need to initialize a loop. We are going to append the letter from the shorter word each time for i.
The loop will persist while the length of i is less than the length of word one and 2. We are not doing the first letter of each word then the second of each, it is ever other letter of the first then every other letter
of the second then concatinate

'''