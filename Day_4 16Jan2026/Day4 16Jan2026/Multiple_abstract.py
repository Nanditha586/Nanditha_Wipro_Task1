from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def loan(self,amount):
        pass
    @abstractmethod
    def interest(self,amount,time):
        pass
class SBI(Bank):
    def loan(self,amount):
        print("Loans can be approved in SBI")
        repayment=amount+(amount*2)
        print("Loan amount to be repayed=",repayment)
    def interest(self,amount,time):
        print("Interest can be approved in SBI")
        interest=(amount*time*0.5)/100
        print("interest amount=",interest)

class ICICI(Bank):
    def loan(self,amount):
        print("Loans can be approved in ICICI")
        repayment=amount+(amount*3)
        print("Loan amount to be repayed=",repayment)
    def interest(self,amount,time):
        print("Interest can be approved in ICICI")
        interest=(amount*time*1)/100
        print("interest amount=",interest)
s=SBI()
s.loan(50000)
s.interest(20000,12)
i=ICICI()
i.loan(50000)
i.interest(20000,12)
