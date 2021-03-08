
def calculate_days (years, months, days):
    print ("years = ", years, "months = ", months, "days = ", days)
    num_days = 365 * years + 30 * months + days
    if years > 4:
        num_days += 1
    return num_days

def get_dates():
#    print("This program determines your age in days")
#    bdate = input("Enter your birthdate in mm/dd/yyyy")
#    tdate = input("Enter today's date in mm/dd/yyyy")
#    '03/08/2021'
    bdate = ''
    tdate = ''
    dates = user_input(bdate, tdate)
    print(dates)
    bdate = dates[0]
    tdate = dates[1]
    bdate_list = bdate.split('/')
    tdate_list = tdate.split('/')
    for i in range(len(bdate_list)):
        bdate_list[i] = int(bdate_list[i])
        tdate_list[i] = int(tdate_list[i])
    age = []
    age.append(tdate_list[-1] - bdate_list[-1]) #years
    age.append(tdate_list [0] - bdate_list [0]) # months
    age.append(tdate_list[1] - bdate_list[1]) #days
    return age

def user_input(birthdate, todays_date):
    print ("This program calculates your age in days")
    birthdate = input("Enter your birthdate in mm/dd/yyyy format")
    todays_date = input("Enter todays date in mm/dd/yyyy format")
    l = []
    l.append(birthdate)
    l.append(todays_date)
    return l

if __name__ == "__main__":
#    yrs = 23
#    mos = 3
#    days = 7
#    age_in_days = calculate_days(yrs, mos, days)

# prompt user for today's date and user birthday
# and I'll get the values for years, months and days
# that way

# great place for another function

    age_list = get_dates()
    yrs = age_list[0]
    mos = age_list[1]
    days = age_list[2]
    age_in_days = calculate_days(yrs, mos, days)
    print("Your age in days is ", age_in_days)

