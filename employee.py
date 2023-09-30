"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Commission:
    def __init__(self) -> None:
        pass

    def get_commission(self) -> int:
        pass

    def __str__() -> str:
        pass


class Employee:
    def __init__(self, name: str, commission: Commission) -> None:
        self.name = name
        self.commission = commission

    def get_pay(self) -> int:
        pass

    def __str__(self) -> str:
        pass


class SalariedEmployee(Employee):
    def __init__(self, name: str, salary: int, commission: Commission = None) -> None:
        super().__init__(name, commission)
        self.salary = salary

    def get_pay(self) -> int:
        return self.salary + (self.commission.get_commission() if self.commission else 0)
    
    def __str__(self) -> str:
        commissionString = str(self.commission) if self.commission else ""
        return f"{self.name} works on a monthly salary of {self.salary}{commissionString}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name: str, hours: int, rate: int, commission: Commission = None) -> None:
        super().__init__(name, commission)
        self.hours = hours
        self.rate = rate

    def get_pay(self) -> int:
        return self.hours * self.rate + (self.commission.get_commission() if self.commission else 0)
    
    def __str__(self) -> str:
        commissionString = str(self.commission) if self.commission else ""
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour{commissionString}. Their total pay is {self.get_pay()}."


class BonusCommission(Commission):
    def __init__(self, bonus: int) -> None:
        super().__init__()
        self.bonus = bonus

    def get_commission(self) -> int:
        return self.bonus
    
    def __str__(self) -> str:
        return f" and receives a bonus commission of {self.bonus}"
    

class ContractCommission(Commission):
    def __init__(self, contracts: int, rate: int) -> None:
        super().__init__()
        self.contracts = contracts
        self.rate = rate

    def get_commission(self) -> int:
        return self.contracts * self.rate
    
    def __str__(self) -> str:
        return f" and receives a commission for {self.contracts} contract(s) at {self.rate}/contract"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalariedEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalariedEmployee('Renee', 3000, ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalariedEmployee('Robbie', 2000, BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, BonusCommission(600))
