    def totalMoney(self, n: int) -> int:
        count_day = 0
        total_money = 0
        monday = 0
        while n > 0:
            count_day += 1
            
            #per week
            if count_day > 7:
                count_day = 1
                monday += 1
                
            total_money += count_day + monday
            n -= 1
        return total_money
