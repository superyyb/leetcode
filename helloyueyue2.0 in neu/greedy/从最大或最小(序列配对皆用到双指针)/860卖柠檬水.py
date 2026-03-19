class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        charge_5 = charge_10 = 0
        for i, bill in enumerate(bills):
            if bill == 5:
                charge_5 += 1#计算我的零钱
                continue
            elif bill == 10:
                charge_5 -= 1
                charge_10 += 1
                if charge_5 < 0:
                    return False
            elif bill == 20:#优先找10块的charge
                if charge_10 > 0:
                    charge_10 -= 1
                    charge_5 -= 1
                else:
                    charge_5 -= 3
                if charge_5 < 0 or charge_10 < 0:
                    return False
        return True