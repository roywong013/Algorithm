class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            y = list(str(x))
            y.reverse()
            return int("".join(y)) == x
