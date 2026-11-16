'''
Implement a program that prompts the user to insert a coin,
one at a time, each time informing the user of the
amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume the
user will only input integers, and ignore any integer that
isn't an accepted denomination.
'''

def main():

    amount = int(input("Please insert 50 cents: "))

    while amount < 50:
        print("Your short", 50 - amount, "cents")
        amount2 = int(input("Please add more: "))
        amount = amount + amount2
        
        if amount > 50:
            print("Your change is: ", amount - 50)

    else:
        print("Thank you for your purchase.")

main()