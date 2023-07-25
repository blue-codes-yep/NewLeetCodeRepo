class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_dict = {}
        
        for char in magazine:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for char in ransomNote:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            else:
                return False
        
        return True