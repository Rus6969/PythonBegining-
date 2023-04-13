
int_list = [1,2,3]
#in pytho in list we can store diferent datatypes
mixed_list=[1,2.0,"text"]

len(mixed_list)

print(int_list[0])

#lastone
print(int_list[-1])

listNames = ["Inna","Alan", "Ruslan", "Elena", "rustam","Olga"]
lastNames =["Gorbunova","Samatov", "Durmanenko", "Shaibulatova", "Nurmahamatov","Gregor"]
#till that index
print(listNames[:1])

# all after this index
print(listNames[1:])

#third argument where we give step  from zero till six each second
print(listNames[0:6:2])

#concatatnation lists
First_and_lastnames = listNames+lastNames
print(First_and_lastnames)
First_and_lastnames[0]="Adaa"
First_and_lastnames.append("Bob")
print(First_and_lastnames)

#delet last from end
print(First_and_lastnames.pop())
#specify index
First_and_lastnames.append("Bob")
First_and_lastnames.pop(0)

letter = ["AA1","bb","ab","cc"]
print(letter)
letter.sort()
print(letter)

numbers=[0,5,8,-6,1,4,3,7,7,5,6]
print(numbers)
numbers.sort()
print(numbers)
# this reverse is not in descending order
numbers.reverse()
print(numbers)
# Descending order
numbers.sort(reverse=True)
print(numbers)
# add at specific index of a list
numbers.insert(1,22)
print(numbers)
# will return under which index located specific object
print(numbers.index(8))

#return number of repepetive number how many time appers in list
print(numbers.count(7))

# Sorting in Python



