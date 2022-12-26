from TUIUtilities import *

def test1():
    print("test1")

def test2():
    print("test2")

def test3():
    print("test3")


menu = SelectorMenu("Menu principal")
test = SelectorMenu("Menu test")

test.add("test1", SelectorFunction(test1))
test.add("test2", SelectorFunction(test2))

menu.add("test", test)
menu.add("test3", SelectorFunction(test3))

menu.execute()