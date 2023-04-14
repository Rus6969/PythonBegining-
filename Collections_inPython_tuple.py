# analog array
# ARE USED TO PROTECT DATA
words = ("book", "bottle", "pan", "waffel", 4, 0)
# can NOT be modified


person = ("Ruslan", "SmTOV", 32)
len(person)
print(person[1])
players = [("Lebron", 38, 3700000), ("Curry", 34, 2600000)]
print(players[0])

print(words[2])


# named tuple to search by name not index

from collections import namedtuple

Player = namedtuple("Player", "name age points")
players = [Player("Lebron", 38, 3700000), Player("Curry", 34, 2600000)]

print(players[0].name)
print(players[0].age)
print(players[0].points)
print(type(players[0].age))
