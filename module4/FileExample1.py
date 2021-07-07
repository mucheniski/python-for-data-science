with open("../files/names.txt","r") as File1:
    file_names = File1.read()
    names = File1.readlines()
    print(names)
    print(file_names)
print(File1.close())
print(file_names)
