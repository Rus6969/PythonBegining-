numbers =[1,2,3,4,5]
print(numbers)

# for x in numbers:
#     print(x)


for i in numbers:
    print(i*3)

    print(range(0, 5))

print(type(range(100)))

for seq in range(10):
    print(seq)



for i in range(1,6):
    if i%2==0:
     print(f"{i} is even")
    else:
        print(f"{i} is odd")


        nums = [1,2,3,4,5]
        for i, item in enumerate(nums):
            nums[i]*=2
            print(item)
            print(i)
            print(nums)


person = ("Ruslan",'samatov', 31)
for item in person:
    print(item)


#tuple
    persons=[("inna",29),("ruslan",31)]
    for(name,age) in persons:
        print(f"{name} is {age} old")


        #dictiomary
        players = {"Lebron": 38,
                   "Luka": 24,
                   "Kawai": 32,
                   "Yaniss": 30}


        for item in players.items():
            print(item)



        # for item in players:
        #     print(item)

        for k,v in players.items():
                print(f"{k} is mvp in age {v}")


#all pairs sum equals 0
list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]
# empty list
pairs=[]
for x in list1:
    for y in list2:
        cursum = x+y
        if cursum == 0:
            pairs.append((x,y))

            print(pairs)
            print(type(pairs))







