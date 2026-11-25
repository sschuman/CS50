"""
Prompt for a date and convert it to YYYY-MM-DD format.
"""


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month, day, year = map(int, date.split("/"))
            else:
                month_name, rest = date.split(" ", 1)
                day_text, year_text = rest.split(", ")
                month = months.index(month_name) + 1
                day = int(day_text)
                year = int(year_text)

            if not 1 <= month <= 12 or not 1 <= day <= 31 or year < 1:
                continue

            print(f"{year:04}-{month:02}-{day:02}")
            break
        except (ValueError, IndexError):
            continue


main()