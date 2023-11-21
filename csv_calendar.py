from calendar import monthcalendar

months = ["", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def year_input():
    while True:
        try:
            year = int(input("For which year do you want to generate a calendar? (4 digit number):"))
            if year >= 1000 and year <= 10000:
                return year
            else:
                print("That's not an integer 4 digit number...")
        except:
            print("That's not a number at all...")

def get_month_text(year, month_index):
    month = monthcalendar(year, month_index) # list of weeks, which are lists of days
    text = f"{months[month_index]} {year}{6*','}\n" # month name and year
    text += ",".join(days_of_week) + "\n" # days of a week

    for week in month:
        week_without_zeros = []
        for day in week:
            if day == 0:
                week_without_zeros.append("") # we want blank cells
            else:
                week_without_zeros.append(str(day))
        week_row = ",".join(week_without_zeros)
        text += week_row + "\n"

    text += "\n" # split months

    return text

year = year_input()

with open(f"calendar-{year}.csv", "w") as file:
    for month_index in range(1,13):
        file.write(get_month_text(year, month_index))

