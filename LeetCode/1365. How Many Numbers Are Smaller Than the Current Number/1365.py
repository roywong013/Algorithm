    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for x in nums:
            count = 0
            for y in nums:
                if x > y:
                    count += 1
            arr.append(count)
        return arr
