class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        biggest = max(candies)
        arr = []
        for i in candies:
            arr.append(i + extraCandies >= biggest)
        
        return arr
