from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
    
        for s in strs:
        # Count the frequency of each character in the string
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
        
        # Convert the frequency list to a tuple to use as a dictionary key
            key = tuple(freq)
        
        # Append the string to the corresponding list in the dictionary
            anagram_groups[key].append(s)
    
    # Return the values of the dictionary as a list of lists
        return list(anagram_groups.values())


        