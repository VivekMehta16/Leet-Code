from collections import defaultdict
class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # anagram = defaultdict(list)
        # for word in strs: 
        #     keys = ''.join(sorted(word))
        #     anagram[keys].append(word)
        
        # return list(anagram.values()) ---> Sorted 

        #Using Hashmap
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 
            res[tuple(count)].append(s)
    
        return res.values()