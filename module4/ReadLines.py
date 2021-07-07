with open("../files/names.txt","r") as File1:

    # Read all lines
    # file_stuff = File1.readlines()
    # print(file_stuff)

    # Read only one line
    # file_stuff = File1.readline()
    # print(file_stuff)
    #
    # file_stuff = File1.readline()
    # print(file_stuff)

    # Especify a number of caracters
    file_stuff = File1.readlines(2)
    print(file_stuff)

    file_stuff = File1.readlines(4)
    print(file_stuff)