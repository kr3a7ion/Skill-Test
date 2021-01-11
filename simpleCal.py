#!/usr/bin/env python3

#Build a simple cal i want the user to add two number
#But the cal give result but ask  for more input if any

print("Your Aviable Maths Operators are x / - +")

powr = input("Enter Maths: ")

usr_inp1 = int(input("Enter 1st Digit: "))
usr_inp2 = int(input("Enter 2nd Digit: "))
print("\n")

def logicc(*args):

    def logicc2():
        usr_inp3 = int(input("Enter next Digit: "))

    if powr == "+":
        add = usr_inp1 + usr_inp2
        print("Result = " + str(add))

    elif powr == "-":
        sub = usr_inp1 - usr_inp2
        print("Result = " + str(sub))

    elif powr == "/":
        div = usr_inp1 / usr_inp2
        print("Result = " + str(div))

    else:
        powr == "*"
        mul = usr_inp1 * usr_inp2
        print("Result = " + str(mul))

    r = input("Enter Maths or Hit E and Enter to End: ")

    def cout(*args):

        if r == "x":
            powr = r
            logicc2()

        elif r == "/":
            powr = r
            logicc2()

        elif r == "+":
            powr = r
            logicc2()

        elif r == "-":
            powr = r
            logicc2()

        else:
            exit("Program Complete")

    print("\n")
    logicc()


    # if powr == "x" or "/" or "-" or "+":
    #     logicc2()
    #
    # else:
    #     print(powr)
    #     logicc()
logicc(usr_inp1, usr_inp2)
