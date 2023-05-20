# in java analog maps

players ={"Lebron":38,
           "Luka":24,
            "Kawai":32,
          "Yaniss":30}

# get access to dict
print(players["Lebron"])

print(players.get('Kawai'))
#if exists will return as get if there is not will add with a  value none
players.setdefault("Harden")
print(players)

# add to dict
players["JA"]=24
print(players)

#delete or pop
#del players["Luka"]

#players.pop("Luka")

#will delet last one
print(players.popitem())

print(players)
# will return only keys
keys= players.keys()
print(type(keys))
print(keys)

#to save Keys keys to list
listofKeys =list(players.keys())
print(type(listofKeys))
print(listofKeys)
# create sorted list of keys
sortedListofKeys =sorted(players.keys())
print(sortedListofKeys)

# to check is in a list or noe

print("Lebron"in players)
print("Curry" not in players)

# returns values
vals = players.values()

valsList = list(players.values())
print(valsList)

players_cppy = players.copy()
print(players_cppy.values())

for k,v in players_cppy.items():
    print(k,v)

