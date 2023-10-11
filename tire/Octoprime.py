from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self,condition):
        self.condition = condition
    def needs_service(self):
        sum = 0
        for item in self.condition:
            sum += item
        return sum >= 3