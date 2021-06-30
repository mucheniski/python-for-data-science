# Sets are type of collections
# This means that like Lists an Tuples you can input different python types

# Unlike Lists and Tuples they are unordered
# this means sets do not record element position

# Sets only have unique elements
# this means there is only one of a particular element in a set

# to define a set you use curly brackets, even if you put duplicated values, their not are duplicate in a set
Set1 = {"pop", "rock", "soul", "rock"}
print(Set1)

# TypeCasting a list into a set
albumList = ["Michael Jackson", "pop", "pop"]
albumSet = set(albumList)
print(albumSet)

# Adding elements
bandsSet = {"Metallica", "AC/DC", "Guns"}
bandsSet.add("Nirvana")
bandsSet.add("Guns")
print(bandsSet)

# Removindo item
bandsSet.remove("Guns")
print(bandsSet)

# Verify itens in a set
"Nirvana" in bandsSet # True
"Guns" in bandsSet # False

# Intersection beetwen sets, all the diferent elements are removed, only the same can to a new set
# Are representated by &
set1 = {"Diego", "Bruna"}
set2 = {"Diego", "Noah", "Bruna", "Livia"}
set3 = set1 & set2
print(set3)

# Union
set3 = set1.union(set2)
print(set3)

# Issubset returns True if a subset has values that conatins in first set
print(set1.issubset(set2)) # True
