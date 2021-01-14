import os


start = os.getcwd()
os.mkdir("Dir_1")
os.chdir("Dir_1")
dir1_f = os.getcwd()
dir_list = ["Dir_2", "Dir_3"]
for i in dir_list:
	os.mkdir(i)
os.chdir("Dir_3")
dir3_f = os.getcwd()
os.mkdir("Dir_4")
os.chdir("Dir_4")

user_answer = input("Do you want to delete the folders? Print 'Y' for yes or 'N' for no: ")

while user_answer.lower() != "y" and user_answer.lower() != "n":
	print("Invalid input.")
	user_answer = input("Do you want to delete the folders? Print 'Y' for yes or 'N' for no: ")

if user_answer.lower() == "y":
	os.chdir(dir3_f)
	os.rmdir("Dir_4")
	os.chdir(dir1_f)
	for i in dir_list:
		os.rmdir(i)
	os.chdir(start)
	os.rmdir("Dir_1")
	print("All the folders are deleted.")
else:
	print("I haven't deleted any folder.")