print('Ruslan')

print(5+5)
# division always returns Float
print(6/2)

# sum with float will return float
print(6+2.0)

print (round(1.2*2,2))

#remimder
print(4%2==0)

# stepen
print(2**4)


print ('Rula')

#variable
x=3
print(x)
# data type
print(type(x))


a = True
print(type(a))

print(5<8)
a = None
print(a)

print(type(a))
name = "Rs"
print(name)

print("I\'m Russlan and I'm a\"strong\" programmer")

print(r'""""'""'//==p=-=')


str("hello")
name = str("ruslan")
print(name[0])
print(name[-2])

name = "Ruslam"

#print(name[2:4])

programmLanguage = "I love Java more than Python"

#print everytinng from second index
print(programmLanguage[2:])

# print till 5th indexes
print(programmLanguage[:5])

#print each second add step, each step
print(programmLanguage[::2])
# print from till
print(programmLanguage[0:6])

#third argument where we give step  from zero till six each second
print(programmLanguage[0:6:2])


# Concatanation
print("my name is " + "Ruslan")

hello = "hello"
world = " world"
print(hello+world)

# Operators and or
print(1<2 and 0>-1)

print(len(hello) < len(world) or len(world) == 5)

# read files in Python
file = open("main.py")
#returns String
data = file.read()
print(data)
#returns to beginig of a page
file.seek(0)


#if we do not want return string in file we cam use  list

lines = file.readlines()
print(type(lines))
print(lines)

file.close()
#print(file.closed())


#with open ("/Users/ruslansamatov/Desktop/Sample.txt", mode = 'a') as sample_file:
#    sample_file.write("Inna: Boss")

  #  print(sample_file.read())


with open("test_sample.txt",mode='w+') as test:
    test.write("Inna is Alan's mom")
    test.seek(0)
    print(test.read(

    ))

