import os,sys

x = 10
y=20  # bad spacing

def add(a,b): 
  return a+b    # bad indentation

def Unused(foo, bar):  # unused args 
    temp = 42   # unused variable
    return None

def main():
    z = add(x,y)
    print("Result is " + str(z))  # ok
    if True == True:   # comparison with constant
        print("Always true")
    for i in range(5):
        print("hello world") # unused loop variable i
main() 