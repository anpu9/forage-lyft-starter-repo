from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self,condition):
        self.condition = condition
    def needs_service(self):
        return sum(self.condition) >= 3.0