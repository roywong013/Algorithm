class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1+nums2
        arr.sort()
        if len(arr) % 2 == 0:
            return ((arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])/2)
        else:
            return arr[round((len(arr)+1)/2)-1]
