agesList=[12,45,23,12,89,18]

def isAnAdult(age):
    return age>=18

filter(isAnAdult,agesList)    

lsitResults = list(filter(isAnAdult,agesList) )
print(lsitResults)


# lamdbda transtion we can save lambda in variable 
is_Adault_Lambda = lambda age: age>=18
 # we can add filter 
list(filter(is_Adault_Lambda,agesList))
# with multiple parameters 
multiplyer = lambda x,y: x*y


print(multiplyer(4,8))

