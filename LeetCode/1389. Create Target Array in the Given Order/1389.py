    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        i = 0
        for x in index:
            arr.insert(x,nums[i])
            i += 1
        return arr
