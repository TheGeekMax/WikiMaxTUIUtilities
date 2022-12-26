from blessed import Terminal

term = Terminal()

#fonction annexes
def printAt(text,x,y):
    with term.location(x=x, y=y):
            print(text)

def clearScreen():
    print(term.home + term.clear)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def tempLoop():
    while True:
        pass

# objet principal pour le selecteur 
class Executable:
    def __init__(self):
        pass

    def execute(self):
        pass

class SelectorFunction(Executable):
    def __init__(self, function):
        self.function = function

    def execute(self):
        self.function()

class SelectorMenu(Executable):
    def __init__(self,title):
        self.key  = [] # liste des noms des fonctions
        self.menu = [] # liste d'objets Executable
        self.title = title

    def add(self, key, executable):
        self.key.append(key)
        self.menu.append(executable)
    
    def execute(self):
        clearScreen()
        var = ''
        choosen = 0
        with term.cbreak():
            while var == "" or not var.name == "KEY_ENTER":
                printAt(self.title,0,1)
                for i in range(len(self.key)):
                    printAt(["-",">"][int(i==choosen)]+self.key[i],1,4+i)
                var = term.inkey(timeout=1)
                if var and var.is_sequence:
                    if var.name == "KEY_UP":
                        choosen = clamp(choosen -1,0,len(self.key)-1)
                    elif var.name == "KEY_DOWN":
                        choosen = clamp(choosen +1,0,len(self.key)-1)
            self.menu[choosen].execute()

