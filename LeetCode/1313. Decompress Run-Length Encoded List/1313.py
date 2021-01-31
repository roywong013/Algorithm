    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for x in range(len(nums)):
            if x % 2 == 0:
                for y in range(nums[x]):
                    arr.append(nums[x+1])
            
            else: 
                continue
        return arr
