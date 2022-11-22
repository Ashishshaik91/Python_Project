from function import Function
from art import logo1


print(logo1)

is_on = True
while is_on:
    try:
        func = Function()
        func.multiplants()
        func.result()
    except ValueError:
            print("Please insert only natural numbers.")
    finally:
        if input("\nWant to do it again or want to exit?!! Press Y to continue or N to stop.\n").lower() == "n":

            is_on = False
            input('press ENTER to exit and make sure remember them before clicking.')







