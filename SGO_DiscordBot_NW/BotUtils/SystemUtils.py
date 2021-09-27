
from colorama import init, Fore, Style , Back
import json;


class PrintDecorators:
    WARNING = [Fore.YELLOW , "Warning: "];
    FAIL = [Fore.RED , "Execution failed: "];
    ERROR = [Fore.MAGENTA, "Error: "];
    NOTATION = [Fore.GREEN, "\t note: "];
    DEFAULT = ["",""];

class DebugWritters:
    ActivityLogFile = "BotActivity.log"
    DebugLogFile = "Debug.log"

def InitializeSystemUtils():
    init(convert=True);

def SysPrint(Text, InSysDecorators = PrintDecorators.DEFAULT):
    print(f'{InSysDecorators[0]}{InSysDecorators[1]}{Text}');



def Serialize(Object , file = None):
    if(file == None or file == ""):
        return json.dumps(Object);


    with open(file , 'w+',encoding='utf-8') as f:
        json.dump(Object,f,ensure_ascii=False,indent=4);


def ReadJsonFile(file):
    with open(file, 'r') as f:
        Data = None;
        try:
            Data = json.load(f)
        except (JSONDecodeError , IOError):
            SysPrint('error parsing '+ file, PrintDecorators.ERROR);
        finally:
            return  Data;


        return Data;