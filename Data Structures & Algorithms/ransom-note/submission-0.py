class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for char in list(magazine):
            if mag_dict.get(char):
                mag_dict[char] += 1
            else:
                mag_dict[char] = 1
        
        for char in list(ransomNote):
            if mag_dict.get(char):
                mag_dict[char] -= 1
            else:
                return False
        
        return True