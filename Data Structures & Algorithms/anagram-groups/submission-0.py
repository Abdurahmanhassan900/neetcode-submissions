class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  

        for word in strs:
            sorted_key = "".join(sorted(word))

            if sorted_key not in groups:
                groups[sorted_key] = []

            groups[sorted_key].append(word)
        
        return list(groups.values())

#First, we create an empty dictionary called groups.
#We loop through each word in the input list strs. 
#For each word, we sort its characters alphabetically 
#using "".join(sorted(word)) to create a sorted_key.
#Next, we check if sorted_key already exists in groups. 
#If it doesn't, we initialize an empty list for that key.
#Then, we append the original word into groups[sorted_key].
#Finally, after the loop finishes, we return list(groups.values()), 
#which gives us all the anagram groups bundled together