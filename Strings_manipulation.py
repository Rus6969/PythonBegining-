
hello = "hello"
world = "world"
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

#partition  devides by separature returns tuples

python1= "Python is fun "

print(python1.partition('is'))
print(python1.partition('not'))


#“Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.”



#str.partition(sep)

#Return type → Tuple

#Example 1: Splits the string at the first occurrence of a sep (delimiter)
colors="red-orange-yellow-purple"
print (colors.partition("-"))
#Output:('red', '-', 'orange-yellow-purple')
#Example 2: The sep is given as a space
s="Hello Python"
print (s.partition(" "))
#Output:('Hello', ' ', 'Python')
#Example 3: If a sep isn’t mentioned, it’ll raise a TypeError
s="Hello Python"
#print (s.partition())
#Output:TypeError: partition() takes exactly one argument (0 given)
#Example 4: If a sep isn’t found in the string, it’ll return a 3-tuple containing the string itself, followed by two empty strings
s="HelloPython"
print (s.partition(" "))
#Output:('HelloPython', '', '')

######################################################################

# FormaT
my_name ="Ruslan"
last_name ="samatov"
print("my name is {}".format(my_name))
print("my name is {} and my last name {}".format(my_name,last_name))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#The format() method formats the specified value(s) and insert them inside the string's placeholder.
#The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
#The format() method returns the formatted string.
name1 = "Inna"
age =30
# we add f to enable formating
print(f"My name is {name1} and Im {age}")

