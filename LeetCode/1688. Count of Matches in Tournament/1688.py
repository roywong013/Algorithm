    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n != 0:
            if n == 1:
                break
            if n % 2 ==0:
                n = n/2
                count += n
            else:
                count += (n-1)/2
                n = (n-1)/2 +1
        return int(count)
