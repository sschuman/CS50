'''
Implement a program that prompts the user for a
vanity plate and then output "Valid" if meets all
of the requirements or "Invalid" if it does not. 
Assume that any letters in the user's input will be
uppercase. Structure your program per the below, wherein
"is_valid" returns "True" is "s" meets all requirements 
and "Falses" if it does not. Assume that "s" will be a
"str". You're welcome to implement additional functions
for "is_valid" to call (e.g., one function per requirement).
'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha() or not s.isalnum():
        return False

    for index, character in enumerate(s[2:], start=2):
        if character.isdigit():
            return character != "0" and s[index:].isdigit()
    return True


if __name__ == "__main__":
    main()