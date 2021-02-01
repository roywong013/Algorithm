    def heightChecker(self, heights: List[int]) -> int:
        arr = heights.copy()
        arr.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                count += 1
        return count
