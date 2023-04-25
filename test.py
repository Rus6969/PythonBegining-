# y = int(input("enter range even odd "))
#
# for i in range(y+1):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i}is odd ")

# sum = 0
# for i in range(10):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
#     else: continue
# print(sum)




# Consider the list of integers
mylist1=[20,40,32,6,78,90]

# Using sum()
print("SUM: ", sum(mylist1))
#list comprehension
limit = int(input("enter ranfe for numbers"))
total_sum=sum([i for i in range (limit) if i % 3 == 0 or i % 5 == 0])
print(total_sum)