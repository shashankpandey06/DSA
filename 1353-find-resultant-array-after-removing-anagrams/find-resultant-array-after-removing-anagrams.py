class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]  # Always keep the first word
        
        for i in range(1, len(words)):
            # Compare sorted versions to detect anagrams
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])
                
        return res
