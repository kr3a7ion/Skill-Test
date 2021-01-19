#!/usr/bin/env python3
import os

#create a todo list
print("########## --> KREATION'S TODO-LIST <-- ##########")
print("########## --> CREATE YOUR DAILY LIST <-- ########## \n")

def_directory = os.getenv("HOME") +  "/Documents"

def dootts():
    dott = list(range(1, 6))
    # print("Processing.")
    for s in dott:
        print("Processing", end="")
        print("." * s)

    print("\nDone 'Saved sucessfully'")

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
    dootts()

    print("Document Processed And Saved at: " + "'" + file_path + "'")

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
        user_folder_name = (os.getenv("HOME") + input("Specify Folder name: "))
        def_directory = user_folder_name
        fi_le()

    else:
        print("Please Enter 'D' Or 'C' to Continue")
        dir_check()

def file_path():
    global file_dir
    if choice == "1":
        enter_file_name = input("Enter File Name: ")
        print('\n')

    else:
        if choice == "3":
            enter_file_name = input("Enter file name you want to open and Append to: ")
            print('\n')

    file_dir = os.path.join(def_directory, enter_file_name + ".txt")

    print("Displaying file at:", file_dir)
    op = open(file_dir, 'r')
    for file in op:
        print(file, end='')

    op.close()

def d_if_function():
    if choice == "1":
        file_path()
        print('\n')
        print(input("Hit Enter Key to perform another action Or CTRL-Z to STOP \n"))
        print('\n' * 50)
        i_tire()

    elif choice == "2":
        dir_check()
        print('\n')
        print(input("Hit Enter Key to perform another action Or CTRL-Z to STOP"))
        print('\n' * 50)
        dootts()
        i_tire()

    elif choice == "3":

        file_path()

        op = open(file_dir, 'a')
        new_num = int(input("Coutinue from Number: \n"))
        addNum_list = int(input("Numbers of list you want to add: \n"))
        cout_num = list(range(new_num, (addNum_list + new_num), 1))
        num_list_gen = list(range(1, (addNum_list + 1)))

        for i in cout_num:
            u = input(("=>" + str(i) + ". "))
            op.write((str(i) + ". " + u + "\n"))

        op.close()

        print(f"You have sucessfully added {addNum_list} new items.")
        print("Displaying file at:", file_dir)
        op = open(file_dir, 'r')
        for file in op:
            print(file, end='')
        op.close()
        print('\n')
        dootts()
        print(input("Hit Enter Key to perform another action\n Or CTRL-Z to STOP"))
        print('\n' * 50)
        i_tire()

    else:
        print('\n')
        print("Please enter the correct key value Or CTRL-Z to STOP \n")
        i_tire()

#This entire choose session takes the useres input from choice and carry out their option
def choose():
    #Ask the user for their work choice
    print("\n Select from Option 1 - 3 below")
    print("1- To Open existing file")
    print("2- To Create New list")
    print("3- To Open and Append to file")
    print("To Quit Hit Ctrl + Z \n")

    # d_if_function()
def i_tire():
    global choice
    choose()
    choice = input("What do you want to Do?: \n => ")
    d_if_function()

i_tire()
print("\n")
print("===============> End <===============")
