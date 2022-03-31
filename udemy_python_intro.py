#What is a prgramming langunage?
'''
What language does computer speak - binary 1 and 0, on and off, true and false
some language are lower levels others are higher levles to human languahe
Assembly - close to machine language
Python - close to humnans, Javascript, phd, C#
- Python is an interpeting language (interpretor), goes line by line of code
- Translater - takes the entire and translate the code to binary into the machine langauge
For python, the interpeting langauge is cpython
jython - translator in Javascript
pypy translation machine written in python.

Python setup on Machines.

'''
def  add(*arg):
    return sum(arg)

print(add(1,2,3,4,5,6,7))

print(add(*[10,10,10,10,10,10,10,10]))

print(add(**{1:"Adonyo",2:"Emmanuel",2:"Nike",3:"Addidas"}))
