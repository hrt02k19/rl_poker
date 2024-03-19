class HandRank:
    rank_names = [
        "High Card",
        "Pair",
        "Two Pair",
        "Three of a kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a kind",
        "Straight Flush",
        "Royal Flush"
    ]

    def __init__(self, strength, *card_nums):
        if not self._validate(strength, card_nums):
            raise ValueError
        self.strength = strength
        self.card_nums = tuple(card_nums)
    
    def _validate(self, strength, card_nums):
        correct_card_nums = [5, 4, 3, 3, 1, 5, 2, 2, 1, 0]
        return correct_card_nums[strength - 1] == len(card_nums)
    
    def _rename_card_num(self, num):
        if num == 14:
            return "A"
        if num == 13:
            return "K"
        if num == 12:
            return "Q"
        if num == 11:
            return "J"
        return num
    
    def __str__(self):
        return str((self.strength, *self.card_nums))

    def __repr__(self):
        output = self.rank_names[self.strength - 1]
        if self.strength == 9:
            output += f", {self._rename_card_num(self.card_nums[0])} high"
        if self.strength == 8:
            output += f", {self._rename_card_num(self.card_nums[0])}s"
        if self.strength == 7:
            output += f", {self._rename_card_num(self.card_nums[0])}s and {self._rename_card_num(self.card_nums[1])}s"
        if self.strength == 6:
            output += f", {self._rename_card_num(self.card_nums[0])} high"
        if self.strength == 5:
            output += f", {self._rename_card_num(self.card_nums[0])} high"
        if self.strength == 4:
            output += f", {self._rename_card_num(self.card_nums[0])}s"
        if self.strength == 3:
            output += f", {self._rename_card_num(self.card_nums[0])}s and {self._rename_card_num(self.card_nums[1])}s"
        if self.strength == 2:
            output += f", {self._rename_card_num(self.card_nums[0])}s"
        if self.strength == 1:
            output = f"{self._rename_card_num(self.card_nums[0])} high"
        return output
        
    
    def __eq__(self, other):
        if other is None or not isinstance(other, HandRank):
            return False
        return self.strength == other.strength and self.card_nums == other.card_nums
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.strength < other.strength or (
                self.strength == other.strength and self.card_nums < other.card_nums
            )
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        return not self.__le__(other)
    
    def __ge__(self, other):
        return not self.__lt__(other)