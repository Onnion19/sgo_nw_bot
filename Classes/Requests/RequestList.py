
from Classes.Requests.Request import Request
import BotUtils.SystemUtils as S_utils
import os

class RequestList: 

    def __init__(self):
        self.Requests = {} #dictionary storing {item, [Request]};

    def ToString(self , separator=',') -> str:
        s = "\n"
        for item, requests in self.Requests.items():
            serializedRequests = ""
            for request in requests:
                serializedRequests += separator + request.ToString(separator) + "\n"

            s+= item + "\n"
            s+= serializedRequests + "\n"
        return s

    def ItemRequestString(self, item, separator=','):
        s = ""
        if(self.Requests.get(item)):
            serializedRequests = ""
            for request in self.Requests[item]:
                serializedRequests += separator + request.ToString(separator) + "\n"

            s+= item + "\n"
            s+= serializedRequests + "\n"     
        return s

    def Serialize(self, filePath):
        S_utils.CopyFile(filePath, filePath + ".tmp")
        file = open(filePath, 'w+', encoding="utf-8")
        if(file is None):
            S_utils.SysPrint("Can't open file" + filePath, S_utils.PrintDecorators.ERROR)
            return
        file.write(self.ToString(','))
        file.close()

    def InitFromFile(self, filePath):
        file = open(filePath, 'r', encoding = "utf-8")
        if(file is None):
            S_utils.SysPrint("Can't open file" + filePath, S_utils.PrintDecorators.ERROR)
            return
        S_utils.SysPrint("Recover form file process starts")
        self.Requests = {}
        currentItem = ""
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            l = line.split(',')
            if(len(l) <= 0):
                continue
            S_utils.SysPrint(f'Parsing:\n{l}\n', S_utils.PrintDecorators.NOTATION)
            if(l[0] != "" or len(l) > 1): # there is content
                if(len(l[0]) > 0): #it's an item
                    currentItem = l[0]
                    S_utils.SysPrint(f'Item found:{currentItem}\n')
                else: #is a request
                    request = l[1:]
                    if(len(request) == 2):
                        self.AddRequest(currentItem,request[0] , int(request[1]))
                    else:
                        S_utils.SysPrint(f'Error cant process {request}', S_utils.PrintDecorators.ERROR)
                    

    def ItemExists(self, item) -> str:
        return self.Requests.get(item)

    def RequesterIndex(self, item, Requester) -> int:
         for x in range(len(self.Requests[item])):#Search if the Requestser already has a request done.
                if(self.Requests[item][x].GetRequester() == Requester):
                    return x
         return None

    def AddRequest(self, item, Requester, Ammount): 
        if(Requester == "" or item == "" or Ammount < 1):
            return
        if(self.ItemExists(item) is not None): 
           index = self.RequesterIndex(item, Requester)
           if(index is not None):
                self.Requests[item][index].SetQuantity(Ammount) #Update the existing list entry
           else:
               self.Requests[item].append(Request(Requester, Ammount)) #Add a new entry to the list
        else:
           self.Requests[item] = [Request(Requester, Ammount)]#Add a new entry to the dictionary

    def RemoveRequest(self, item, Requester, Ammount=999999): 
        if(Ammount < 0 or not self.ItemExists(item)):
            return
        
        index = self.RequesterIndex(item, Requester)
        if(index is not None):
            request = self.Requests[item][index]
            request.ChangeQuantity(-Ammount)
            if(request.GetQuantity() < 1):
                self.Requests[item].pop(index)
                if(len(self.Requests[item]) == 0):
                    self.Requests.pop(item)

    def WipeData(self):
        self.Requests = {}

    def SearchUserRequests(self, user) -> str:
        s = ""
        for item , requestList in self.Requests.items():
            for request in requestList:
                if(request.GetRequester() == user):
                    s += "\n\t" + item + "\t" + str(request.GetQuantity())

        return s

    def RemoveAllUserRequests(self, user) -> str:
        s = ""
        for item , requestList in self.Requests.items():
            for request in requestList:
                if(request.GetRequester() == user):
                     s += "\n\t" + item + "\t" + str(request.GetQuantity())
                     requestList.remove(request)
                     break

        for item , requestList in dict(self.Requests).items():
            if(len(requestList) <= 0):
                self.Requests.pop(item);
        return s
