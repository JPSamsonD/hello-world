# Use the Open method to open a file
from os import close


my_file_object = open("myfile.txt", "r")
print("Read the whole file at once:")
print(my_file_object.read())
print("\n")
# Close the file
my_file_object.close()
