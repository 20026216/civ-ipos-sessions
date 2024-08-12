class StringNumValue:
    def __init__(self, letter):
        self.letter = letter

    def letter_to_position(self):
        position = (ord(str(self.letter).lower()) - ord('a'))
        if position < 0 or position > 26:
            raise ValueError ('Invalid position, please enter alphabets')
        return position

    def set(self, letter):
        """
        Overwrite the value of the string.

        :param s: String to write
        """
        self.letter = letter


obj = StringNumValue("a")
print(obj.letter_to_position())
obj.set(9)
print(obj.letter)