print("\nWriting to file...")

with open("Aaronic_Blessing.txt", "w") as file:
	file.write("The LORD bless thee, and keep thee:\n")
	file.write("The LORD make his face shine upon thee, and be gracious unto thee:\n")
	file.write("The LORD lift up his countenance upon thee, and give thee peace.")

print("\nNow adding the Bible Reference...\n")

with open("Aaronic_Blessing.txt", "a") as file:
	file.write("\n")
	file.write("- Numbers 6:24-26\n\n")

with open("Aaronic_Blessing.txt", "r") as blessing:
	output = blessing.read()
	print(output)
