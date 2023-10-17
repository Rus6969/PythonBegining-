state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona",
              "California", "Colorado", "Connecticut", "District of Columbia", 
              "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", 
              "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", 
              "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", 
              "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", 
              "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

print(state_names[1])
print(state_names[-1])
state_names[1] = "Ruslans State"
print(state_names[1])

state_names.append("INNA STATE ")
print(state_names)
print("==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=")
state_names.extend(["Maken","GBI" ])

print (state_names)

lastnames =["gorbunova","Viak","Samatov", "Goel"]
lastnames.reverse()
lastnames.pop(1)
print(lastnames)
lastnames.remove("gorbunova")
lastnames.insert(1,"Alan")
print(lastnames)
print(lastnames.count("Alan"))
