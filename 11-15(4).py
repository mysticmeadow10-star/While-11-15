#WAP to take integer value from the user, keep asking for integer value, using an infinite loop, untill user enter a proper integer. if user enter a string, keep asking for integer value using infinite loop.


while True:

    try:
        integer = int(input("Enter an integer value:"))
        print("Interger value taken succesfully")
    except:
        print("please enter a valid integer here..")
    else:
        print("Integer value taken succesfully.")
        break
    finally:
        print("No matter what, this codes runs")