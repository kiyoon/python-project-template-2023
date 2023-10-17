from dataclasses import dataclass


@dataclass
class TwoNumbers:
    num_1: int
    num_2: int

    def add(self):
        assert isinstance(self.num_1, int)
        assert isinstance(self.num_2, int)
        return self.num_1 + self.num_2
