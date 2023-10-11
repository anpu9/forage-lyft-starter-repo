from tire.tire import Tire


class Carrigan(Tire):
    def __init__(self, condition):
        self.condition = condition

    def needs_service(self):
        for item in self.condition:
            if item >= 0.9:
                return True
        return False
