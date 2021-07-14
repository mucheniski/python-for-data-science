# the w at the end indicate write, if your file exists it will be overwrited
with open("../files/writed1.txt","w") as FileWrited1:
    FileWrited1.write("This is Line A\n")
    FileWrited1.write("This is Line B\n")

# a means append, in this case the file will not be overwrited, just appended.
with open("../files/writed1.txt","a") as FileWrited1:
    FileWrited1.write("This is Line C\n")


# with a list
lines = ["Line1\n", "Line2\n", "Line3\n"]
with open("../files/writed2.txt","w") as FileWrited2:
    for line in lines:
        FileWrited2.write(line)

# Read one file and write another trouth that
with open("../files/writed1.txt","r") as readedile:
    with open("../files/writed3.txt","w") as writedFile:
        for line in readedile:
            writedFile.write(line)
