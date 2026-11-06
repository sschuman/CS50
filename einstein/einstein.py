# Implement a program in Python that prompts the
# user for mass as an integer (in kilograms) and then
# outputs the equivalent number of Joules as an integer.
# Assume that the user will input the integer.
def main():
	mass = int(input("Please enter the mass in kilograms: "))
	print(mass * 300000000**2)


main()