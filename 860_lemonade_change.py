class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # [5,5,5,10,20]
        # collected = {5:2, 10:1}
        # change-needed = 0,0,0,5

        # [5,5,10,10,20]
        # collected ={5:0, 10: 2}

        # collected = defaultdict(int)
        # for bill in bills:
        #     change_needed = bill - 5
        #     if change_needed == 0: # $0 bill given
        #         collected[bill] += 1
        #     else:
        #         bills_needed = None
        #         has_valid_change = False
        #         if change_needed == 15: # $20 bill given
        #             if collected[10] >= 1 and collected[5] >= 1:
        #                 has_valid_change = True
        #                 bills_needed = [10,5]
        #             elif collected[5] >= 3:
        #                 has_valid_change = True
        #                 bills_needed = [5,5,5]
        #         elif change_needed == 5: # $10 bill given
        #             if collected[5] >= 1:
        #                 has_valid_change = True
        #                 bills_needed = [5]
        #         if not has_valid_change:
        #             return False
        #         collected[bill] += 1            
                
        #         for change_bill in bills_needed:
        #             collected[change_bill] -= 1

        # return True

        # this is a DP problem if bills weren't limited to 5,10,20
        # def find_change_needed(change_needed):
        #     # collected = {5:2, 10:1}
        #     # change_needed = 15
        #     if change_needed == 15:
        #     elif change_needed = 5:
        #     change_needed -= max_bill

        # simpler, hardcoded solution
        fives, tens, twenties = 0,0,0
        for bill in bills:
            change_needed = bill - 5
            if change_needed == 0:
                fives += 1
                
            elif change_needed == 5:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
                
            elif change_needed == 15:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                twenties += 1

        return True               
    