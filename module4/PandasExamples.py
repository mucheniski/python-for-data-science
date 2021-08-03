# Pandas is a popular libary for data analisys
import pandas

# csv_path = '../files/caixa.csv'
# dataFrame = pandas.read_csv(csv_path)
#
# # to examine de first five rows of the dataFile
# dataFrame.head()
#
# print("*"*100)
# print(dataFrame.head())
# print("*"*100)

# create a dataFrame, Album, Released, Length are de headers of the table
songs = {
    'Album':['Thriller', 'Back in Black', 'The BodyGuard'],
    'Released':[1982, 1980, 1997],
    'Length':['00:43:19', '00:42:11', '00:46:36']
}

songs_frame = pandas.DataFrame(songs)

print(songs_frame)

# Print only one column from a frame, we can do the same to another columns ex songs_frame[['Length', 'Album]]
# the result is a new data frame with the selectec columns
print("*"*100)
print(songs_frame[['Length']])

# We can access values from the frame [row, column]
print("*"*100)
print(songs_frame.iloc[0,0])
print(songs_frame.iloc[1,2])
print(songs_frame.iloc[1,1])

# Creating a new dataframe with the selectec rows
print("*"*100)
print(songs_frame.iloc[0:2, 0:3])