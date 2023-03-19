class tileBacktrack:
    def __init__(self, index):
        self.index = index
        self.el = None
        self.outer = None
        self.full = {'ones': 0, 'twos': 0, 'threes': 0, 'fours': 0}

    def setelresponse(self, ones, twos, threes, fours):
        self.el = {'ones': ones, 'twos': twos, 'threes': threes, 'fours': fours}

    def setouterresponse(self, ones, twos, threes, fours):
        self.outer = {'ones': ones, 'twos': twos, 'threes': threes, 'fours': fours}

