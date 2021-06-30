# Usint with Key:Value

albuns = {"Triller":1982, "Back in Black":1980, "The Dark Side of The Moon":1973, "The Bodyguard":1992}

# Recover value
print(albuns["Triller"])

# Add value
albuns["Graduation"]=2008
print(albuns)

# Delete Value
del(albuns["Triller"])
print(albuns)

# Verify value, if exists return True
print("Graduation" in albuns)

# see all the keys
print(albuns.keys())

# see all the values
print(albuns.values())