# Tuples are created with parentesis, and can contains strings, ints and floats
# the type always be Tuple

Tuple1 = (1, 'two', 3.0)
print(type(Tuple1))

# each element can be accessed by a index
print(Tuple1[0])

# The index reveres is also true
print(Tuple1[-1])

# Tuple can be concatenate to
Tuple2 = Tuple1 + ("four", 5.0)
print(Tuple2)

# First 3 elements
print(Tuple2[0:3])

# Last 2 elements
print(Tuple2[3:5])

# Lenght of elements
len(Tuple2)

# Tuples are imutable
# I we can change the tuple only creating a new tuple
Ratings = (1, 5, 2)
RatingsSorted = sorted(Ratings)

# Nesting is whe the tuple containg another tuples
Nasting = (1, 2, ("pop","rock"), (3,4), ("disco",(1,2)))
print(Nasting[2][1]) # rock




