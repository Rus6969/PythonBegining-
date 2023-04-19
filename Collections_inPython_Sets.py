
myFirstSet= set()
print(type(myFirstSet))

myFirstSet.add(1)

print(myFirstSet)


# list with duplicates
my_list =[1,1,1,1,2,2,2,3,3,3,4]
listToset = set(my_list)

print(listToset)
# is subset
set1={1,2,3,4}
set2={1,2,3,4,5}
print(set1.issubset(set2))

print(set2.issuperset(set1))
#do they have they need additional help with some topics , like  how real agile works ,
# all ceremonies prepare them to real work life env  one of the option we can sell real work experience ,
print(set1.isdisjoint(set2))

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)


# combine to set Union
set3 = set1.union(set2)
print(set3)

#intersection will return coommpn
set4 = set1.intersection(set2)
print(set4)

#difference will return only unique between 2

# sets of numbers
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}

# returns items present only in set A
print(A.difference(B))

# Output:  {1, 9}

A1 = {'a', 'b', 'c', 'd'}
B1 = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
result = A.symmetric_difference(B)
print(result)

# Output: {'a', 'b', 'e'}
result = A1.symmetric_difference(B1)
print(result)

# Output: {'a', 'b', 'e'}

#delete remove
set1.add(9)
print(set1)
set1.remove(9)
print(set1)

#discard delete without error
set1.discard(9)
print(set1)

#pop will delte random and returs as a result
print(set1.pop())