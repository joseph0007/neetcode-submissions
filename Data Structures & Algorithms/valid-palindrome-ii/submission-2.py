class Solution:
    def __init__(self):
        self.of_used = False

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        one_off_used = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            elif not self.of_used:
                self.of_used = True
                lres = self.validPalindrome(s[l:r])
                rres = self.validPalindrome(s[l+1:r+1])
                return lres or rres
            else:
                return False
        return True
                
