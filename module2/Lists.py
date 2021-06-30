# A list are represented by Square Brackets
List1 = ["Diego", 3.4, 1986]

# List are mutable and can Nest another lists to
# each element of the list can be accessed by index, and also can nest Tuples

# last 2 elements
print(List1[1:3]) # the last need to be grather than the list size

# Concatenate
List2 = List1 + ["Man", 1.74]
print(List2)

# Extends
List2.extend(["test",3])
print(List2)

# Append add one more element to the list, unlike extend
List2.append(["test",4])
print(List2)

# Change elements
List2[0] = "Mucheniski"
print(List2)

# Delete elements
del(List2[7])
print(List2)

# Convert string to list
List3 = "Diego Mucheniski".split()
print(List3)

List4 = "A,B,C,D".split(",")
print(List4)

# If we have two Lists pointing to same, a change in one afects second list
A = [1,2,4]
B = A
B[0] = 4
print(A)
print(B)

# If you clone a list, a new list are created, in this case list B are not affected if list a are changed
B = A[:]