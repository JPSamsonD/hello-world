from os import close


print("Loop through and read each line using with to open the file: ")

x = 1

with open("myfile.txt") as file:
    for line in file:
        print("Line " + str(x) + ": " +line)
        x += 1
