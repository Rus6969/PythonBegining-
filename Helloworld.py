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


#sintax foramt for place holders % mean place holder where we do pass parameter ( plus concatsanation is bad for memory , better use parameters
print("%s %s" % (hello,world))
print("{} {}"  .format(hello,world))


# duplicate simples
print("a"*7)


#print(2+"text will giv error ")

# to find length len function
print(len(hello))

# print last
print (hello[(len(hello) - 1)])


# count symbols l in word hello
print(hello.count("l"))

# first letter will make Capitalize
print(hello.capitalize())

# to capitalize all   dsmr with lower
print(hello.upper())
# check upper/lowercase
print(hello.isupper())

# find returns index of specific letter if some of them returns first fount

print(hello.find("l"))
#from which index start serch
print(hello.find("o", 3))


#from which and where to end
print(hello.find("l",2,4 ))
#will return indext of e
print(hello.find("el"))

#is line number and text
print("123abc".isalnum())
print("1!abc".isalnum())

# check only text or not
print("Ruslan".isalpha())
#check for space
print("   ".isspace())

#check for empry
empry_string =" "
print(empry_string=="")
print("*******************************")

# check with Operator NOT "" - returns true , "  " returns false
if not empry_string:
    print(" not empty")
else:
    print("empty")


#delete spaces
space_check = "    Ruslan loves  Java      "
print(space_check.strip())

h = "hello"

print(h.startswith("h"))
print(h.endswith("o"))
#splits
split3=h.split("l")
print(split3)
print(type(split3))








