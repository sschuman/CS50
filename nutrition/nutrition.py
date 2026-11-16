'''
Implement a program that prompts users to input
a fruit (case-insensitively) and then outputs the
number of calories in one portion of that fruit,
per the FDA's poster for fruits, which is also available
as text. Capitalization aside, assume that users will input
fruits exactly as written in the poster. Ignore
any input that isn't a fruit.
'''

def main():
    calories = {
        "apple": "130", 
        "avocado": "50", 
        "banana": "110", 
        "cantaloupe": "50", 
        "grapefruit": "60", 
        "grapes": "90", 
        "honeydew mellon": "50", 
        "kiwifruit": "90", 
        "lemon": "15", 
        "lime": "20", 
        "nectarine": "60", 
        "orange": "80", 
        "peach": "60", 
        "pear": "100", 
        "pineapple": "50", 
        "plums": "70", 
        "strawberries": "50", 
        "sweet cherries": "100", 
        "tangerine": "50", 
        "watermelon": "80"}

    fruit = input("Please enter a fruit: ").lower()

    if fruit in calories:
        print(calories[fruit])

main()