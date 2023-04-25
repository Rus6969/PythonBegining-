
x = 0
while x<3:
    print(f"x={x}")
    x+=1
else:
    print("Condition is not met ")


    print("/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/")


    numbers=[1,2,3,4,5,6,7,8,9]
    sum =0
    for n in numbers:
        if n % 2 == 0:
            continue
        else:
            sum += n
            if sum > 10:
                break
            print(sum)

            for x in [0, 1, 2]:
                pass
            pass
#The pass statement is used as a placeholder for future code.

# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
            # pass


        x = int(input("Enter number of start u would like ?"))
        # print('*'* x)
        for i in range(x):
            # to print on a single line The end parameter of the print function is set to an empty string (""), which means that the default
            # newline character at the end of the printed string is suppressed, so all the stars are printed on a single line.
         print("*",end=" ")


