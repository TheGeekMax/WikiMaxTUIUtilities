from TUIUtilities import *

menu = SelectorMenu("Menu principal")
test = SelectorMenu("Menu test")

def test1():
    test.printData("test1").execute()

def test2():
    print("test2")

def test3():
    menu.printData("test3").execute()

menu.add("test", test)
menu.add("test3", SelectorFunction(test3))
menu.add("test4", menu.printData("test4 de chez test4"))

test.add("test1", test.printData("test 1"))
test.add("test2", SelectorFunction(test2))



menu.execute()