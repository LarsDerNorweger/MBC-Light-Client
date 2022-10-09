#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger
#

class Stack(list):
    def __init__(self):
        super().__init__()
        pass

    def pop_first(self):
        if not self.is_empty:
            return self.pop(0)
        else:
            return None

    @property
    def is_empty(self):
        return len(self) <= 0
