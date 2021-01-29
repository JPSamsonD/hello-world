# Use the Open method to open a file
from os import close


my_file_object = open("myfile.txt", "r")

print("Loop through and read each line: ")

i = 1

for line in my_file_object:
    print("Line " + str(i) + ": " + line)
    i = i+1

print("\n")

# Close the file
my_file_object.close()
