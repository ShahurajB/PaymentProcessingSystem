from abc import ABC , abstractmethod

class Payment(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def credit_money(self):
        pass

    # @abstractmethod
    # def set_user_name(self):
    #     pass