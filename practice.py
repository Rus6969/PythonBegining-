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

#combine from first odd with even from second to new list
first_list=[1,2,3,4,5,6,]
second_list=[11,12,13,14,15,16,]
result=[]

odds = sum(i for i in first_list if i % 2!=0)
even = sum(i for i in second_list if i % 2 == 0)
result= odds+ even
print(f"{result}  all toggather")

# Дан список карт. Например, такой:
# current_hand = [2, 3, 4, 10, 'Q', 5]
# В общем и целом, список может содержать следующие значения: 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'.
# У каждой карты есть свой "вес":
# 2, 3, 4, 5, 6 весят +1
# 7, 8, 9 весят 0
# 10, 'J', 'Q', 'K', 'A' весят -1
# Задача: имея список карт (например, см. current_hand выше), посчитать их общий "вес".
# Примечание:  это уже задачка посложнее. Для красивого решения подумайте как вам может помочь здесь словарь.


current_hand = [2, 3, 4, 10, 'Q', 5]
cards_weight={2:1,3:1,4:1,5:1,6:1,7:0,8:0,9:0,10:-1,'j':-1,'Q':-1,'K':-1,'A':-1}

print(sum([cards_weight[i] for i in current_hand]))

