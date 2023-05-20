# import numbers


# numbers=[1,2,3]
# numbers.append(4)
# print(numbers)
# # help will give a description to each method 
# #help(numbers.append)



# #maths functions
# # will make positive
# abs(-1)

# print(max(1,2,3,4,5))
# print(pow(3,2))
# print(sum([1,2,3]))

# h = hex(42)
# o = oct(42)
# b = bin(42)
# print(h)
# print(b)
# print(b)



# #giving true if all expressions are true 
# all_true1= all([True,True, True])
# all_true2= all([True,False, True])
# print(all_true1)
# print(all_true2)

# mvp=[("lebron",6),("embid",1),("Jokic",2)]
# # are all players were mvp more times  _, sign we put to show that we do not need name to indicate that 
# # we are not interested in a particular value. 
# # It is a placeholder that is commonly used when you want to ignore or discard a value.

# # when for loop meets first false loop will stop work  
# result = all(mvpTimes>1 for _, mvpTimes in mvp)

# # here we will go till the end of the loop despite it meets first false  slower than above 
# result2 = all([mvpTimes>1 for _, mvpTimes in mvp])

# #any at leat one is true will returns trrue 
# any_true = any([True,True, True])
# any_true2 = any([True,True, False])

# result = any(mvpTimes<2 for _, mvpTimes in mvp)

# letters = 'abcd'
# numbers = (10,20,30)
# zipped = zip(letters,numbers)
# print(type(zipped))
# print(zipped)
# zipped_list = list(zipped)
# print(zipped_list)


numbers2 = [1, 2, 3]
letters2 = ['a', 'b', 'c']
symbols = ['!', '@', '#']

result = zip(numbers2, letters2, symbols)

for item in result:
    print(item)


    result = list(zip(numbers2, letters2, symbols))
    print(result)
    print(type(result))

