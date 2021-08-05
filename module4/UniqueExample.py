import pandas

released_years = {
    'Released': [1982, 1980, 1973, 1992, 1977, 1976, 1977, 1977]
}

relased_frame = pandas.DataFrame(released_years)

# A new array with only unique values are created
print(relased_frame['Released'].unique())

# Creating a new dataframe with condition
print("="*100)
testDataFrame1 = relased_frame[relased_frame['Released'] >= 1980]
print(testDataFrame1)


# Save a new dataframe in file
testDataFrame1.to_csv("../files/saved.csv")
