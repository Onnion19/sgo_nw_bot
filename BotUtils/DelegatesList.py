
import BotUtils.SystemUtils as Bot_SysUt;


class DelegateList:
    Dictionary = {};

    def AddDelegate(self , InObject, InFunction):

        if(InObject == None or InFunction == None):
            return;

        if(not self.__ExistDelegate(InObject,InFunction)):
            self.Dictionary[InObject] = InFunction;

        assert self.Dictionary.get(InObject) != None;

    def RemoveDelegate(self, InObject):
        self.Dictionary.pop(InObject);

    def Execute(self, **kwargs):
        for Key , Value in self.Dictionary.items():
            Value(**kwargs);

    def __ExistDelegate(self, InObject, InFunction):
        for Objects , Functions in self.Dictionary.items():
            if(Objects == InObject and Functions == InFunction):
                return True;
        return False;