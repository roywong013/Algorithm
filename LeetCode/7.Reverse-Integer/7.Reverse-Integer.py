class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            arr = list(str(x))
            arr.remove("-")
            arr.reverse()
            while arr[0] == "0":
                if len(arr) == 1:
                    break
                arr.pop(0)
            arr.insert(0,"-")
            reverseAns = int("".join(arr))
            if reverseAns>= -2**31:
                return "".join(arr)
            else:
                return 0
        arr = list(str(x))
        arr.reverse()
        while arr[0] == "0":
            if len(arr) == 1:
                break
            else:
                arr.pop(0)
        reverseAns = int("".join(arr))
        if reverseAns <= (2 ** 31) -1:
            return "".join(arr)
        else: 
            return 0
