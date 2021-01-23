class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        ans = 0
        for i in s:
            if i in arr:
                arr = arr[arr.index(i)+1:]
            arr.append(i)
            ans = max(ans, len(arr))
        
        return ans
                
