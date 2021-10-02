
from colorama import init, Fore, Style , Back
import json


class PrintDecorators:
    WARNING = [Fore.YELLOW , "Warning: "]
    FAIL = [Fore.RED , "Execution failed: "]
    ERROR = [Fore.MAGENTA, "Error: "]
    NOTATION = [Fore.GREEN, "\t note: "]
    DEFAULT = ["",""]

class DebugWritters:
    ActivityLogFile = "BotActivity.log"
    DebugLogFile = "Debug.log"

def InitializeSystemUtils():
    init(convert=True)

def SysPrint(Text, InSysDecorators=PrintDecorators.DEFAULT):
    print(f'{InSysDecorators[0]}{InSysDecorators[1]}{Text}')

def CopyFile(From, To):
    os.system(f"cp {From} {To}")

def TupleToString(t, separator=" ") -> str:
   return  separator.join(t);