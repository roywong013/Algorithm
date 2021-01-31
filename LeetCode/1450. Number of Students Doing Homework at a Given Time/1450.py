    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            temp =[]
            for x in range(startTime[i],endTime[i]+1):
                temp.append(x)

            if queryTime in temp:
                count +=1

        return count
