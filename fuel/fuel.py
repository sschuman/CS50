"""
Prompt for a valid fraction and display the fuel gauge reading.
"""


def main():
    while True:
        fraction = input("Fraction: ")

        try:
            x_text, y_text = fraction.split("/")
            x = int(x_text)
            y = int(y_text)

            if x < 0 or y <= 0 or x > y:
                continue

        except (ValueError, ZeroDivisionError):
            continue

        if x * 100 <= y:
            print("E")
        elif x * 100 >= 99 * y:
            print("F")
        else:
            percentage = (200 * x + y) // (2 * y)
            print(f"{percentage}%")

        break


main()