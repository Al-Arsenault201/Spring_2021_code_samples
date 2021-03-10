#This program calculates a user's current age in days

#CONSTANTS
MONTHS = 0
DAYS = 1
YEARS = 2


def calculate_day_of_year(m, d):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = d
    if m == 0:
        return days
    for i in range(m):
        days += months[i]
    return days


def get_a_date():

    date = input("Please enter the date in the form mm/dd/yyyy")
    date_list = date.split('/')
    for i in range(len(date_list)):
#        print(date_list[i])
        date_list[i] = int(date_list[i])
    days = calculate_day_of_year (date_list[MONTHS], date_list[DAYS])
    day = [days, date_list[YEARS]]
    return day


def calculate_age(birthday, today):
    days = 365 * (today[1] - birthday[1]) + today[0] - birthday[0]
    return days



if __name__ == "__main__":
    print("This program calculates your current age in days")
    print("Enter today's date and then your birthday and you'll see the answer")
    today = get_a_date()
    birthday = get_a_date()
    answer = calculate_age(birthday, today)
    print ("Your age in days is ", answer)
