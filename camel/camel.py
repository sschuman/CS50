'''
Implement a program that prompts the user for
the name of a variable in camel case and outputs
the corresponding name in snake case. Assume
the user's inut will indeed be in camel case.
'''

def main():
    camel_case = str(input("Write something in camelCase: "))
    
    def camel_to_snake(camel_case):
        snake_case = ""
        for char in camel_case:
            if char.isupper():
                snake_case += "_" + char.lower()
            else:
                snake_case += char
        return snake_case

    snake_case = camel_to_snake(camel_case)
    
    print(snake_case)



main()