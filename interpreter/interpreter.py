'''
Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point
value formatted to one decimal place. Assume that the user's input will be formatted as x y z, with one space
between x and y and one space between y and z.
'''
def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 3 + 4): ")
    
    # Split the input into components
    x, operator, y = expression.split()
    
    # Convert x and y to floating-point numbers
    x = float(x)
    y = float(y)
    
    # Perform the calculation based on the operator
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        result = x / y
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    
    # Output the result formatted to one decimal place
    print(f"Result: {result:.1f}")

main()