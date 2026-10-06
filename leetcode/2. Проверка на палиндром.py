class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        xcopy = x
        if x < 0: return False
        while x > 0:
            reverse = (reverse * 10) + x % 10
            x = x // 10
        return xcopy == reverse
print(Solution().isPalindrome(212))