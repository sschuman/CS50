"""
Prompt for grocery items and print each item with its count.
"""


def main():
    groceries = {}

    while True:
        try:
            item = input("Enter your item: \n").strip().lower()
        except EOFError:
            break

        if item:
            groceries[item] = groceries.get(item, 0) + 1

    for item in sorted(groceries):
        print(f"{groceries[item]} {item.upper()}")


main()