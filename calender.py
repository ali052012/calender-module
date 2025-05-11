import calendar

def show_month_calendar():
    try:
        year = int(input("Enter year (e.g. 2025): "))
        month = int(input("Enter month (1-12): "))
        if 1 <= month <= 12:
            print("\n" + calendar.month(year, month))
        else:
            print("Invalid month! Please enter between 1 and 12.")
    except ValueError:
        print("Please enter valid numbers.")

def show_year_calendar():
    try:
        year = int(input("Enter year (e.g. 2025): "))
        print("\n" + calendar.calendar(year))
    except ValueError:
        print("Please enter a valid year.")

def main():
    print("📅 Python Calendar App")
    print("1. Show Month Calendar")
    print("2. Show Full Year Calendar")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        show_month_calendar()
    elif choice == "2":
        show_year_calendar()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
