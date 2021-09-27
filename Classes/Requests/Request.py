
class Request:

    def __init__(self, requester="" , ammount=1):
        self.mRequester = requester
        self.mAmmount = ammount

    def GetRequester(self) -> str:
        return self.mRequester

    def GetQuantity(self) -> int:
        return self.mAmmount

    def ChangeQuantity(self, relativeAmount):
        self.mAmmount += relativeAmount
      
    def SetQuantity(self, newAmmount):
        self.mAmmount = newAmmount

    def ToString(self, separator=',') -> str:
        return self.mRequester + separator + str(self.mAmmount);