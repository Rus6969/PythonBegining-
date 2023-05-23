import re


def square(*args):
    return [x*x for x in args]


print(square(1,2,3,45,))


def tripple (*args):
    return [x*3 for x in args]


result = tripple(1,2,3)
print(result)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(type(result))
print(result)
print("========================MAP FUNCTION====================================")

numbers=[1,2,3,4,5]
def square2(number):
    return number*number

#will print hash number objext in a memory 
print(map(square2,numbers))   

for i in map(square2,numbers):
    print(f'{i} number in square')

    #save directly to list 
saveToList=  list(map(square2,numbers))
print(saveToList)
