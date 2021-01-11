#!/usr/bin/env python3
import os.path

#create a todo list
print("########## --> KREATION'S TODO-LIST <-- ##########")
print("########## --> CREATE YOUR DAILY LIST <-- ########## \n")

#This next two lines asks the user's Username
ur = input("Provide Pc Username(Case Sensitive):")
def_directory = "/home/" + ur + "/Documents"


def fi_le():
    x = int(input("Enter The Length of Your To-Do-List: "))

    #this next line of codes should generate the number of list you want
    xf = list(range(1, (x + 1)))

    #This next line asks to save your To-do list in a default dir or create one
    directory = def_directory
    namer = input("Enter File Name: ")
    file_name = namer + ".txt"
    file_path = os.path.join(directory, file_name)

    if not os.path.isdir(directory):
        os.mkdir(directory)

    f = open(file_path, "w+")

    #This next line of code print out the number of line and takes in user To-Do-List
    for i in xf:
        u = input(("=>" + str(i) + ". "))
        f.write((str(i) + ". " + u + "\n"))

    f.close()

    print("\n" * 100)
    print("Document Processed And Saved at: " + "'" + file_path + "'")
    print("Enter Choice or Hit Ctrl + Z to quit")
    choose()

def dir_check():
    global def_directory
    print("\n")
    print("*NOTE: PLEASE NOTE YOUR DEFAULT DIR FOR SAVED FILE IS THE 'DOCUMENTS FOLDER'")
    print("IF YOU WANT TO CHANGE DIR ENTER 'C' TO PROCEED ELSE ENTER 'D' TO USE DEFAULT FOLDER")
    print("\n")

    ask_user = input("Do you want to Proceed with DEFAULT FOLDER: ").upper()

    if ask_user == "D":
        fi_le()

    elif ask_user == "C":
        user_folder_name = ("/home/" + ur + "/" + input("Specify Folder name: "))
        def_directory = user_folder_name
        fi_le()

    else:
        print("Please Enter 'D' Or 'C' to Continue")
        dir_check()

#This entire choose session takes the useres input from choice and carry out their option
def choose():
    #Ask the user for there work choice
    print("\n Select from Option 1 - 3 below")
    print("1- To Open existing file")
    print("2- To Create New list")
    print("3- To Open and Append to file")
    print("To Quit Hit Ctrl + Z \n")

    choice = input("What do you want to Do?: ")

    if choice == "1":
        Enter_file_name = input("Enter File Name: ")
        file_dir= os.path.join(def_directory, Enter_file_name + ".txt")

        print("Displaying file at:", file_dir)
        op = open(file_dir, 'r')
        for file in op:
            print(file, end='')

        op.close()

    elif choice == "2":
        dir_check()

    else:
        choice == "3"
        Enter_file_name = input("Enter file name you want to open and Append to: ")
        file_dir= os.path.join(def_directory, Enter_file_name + ".txt")

        print("Displaying file at:", file_dir)
        op = open(file_dir, 'r')
        for file in op:
            print(file, end='')
        op.close()

        op = open(file_dir, 'a')
        new_num = int(input("Coutinue from Number: "))
        addNum_list = int(input("Numbers of list you want to add: "))
        cout_num = list(range(new_num, (addNum_list * 2 - new_num) + 1, 1))
        num_list_gen = list(range(1, (addNum_list + 1)))

        print(cout_num)
        for i in num_list_gen:
            u = input(("=>" + str(cout_num) + ". "))
            op.write((str(cout_num) + ". " + u + "\n"))

        op.close()
        choose()


choose()


print("\n")
print("===============> End <===============")
