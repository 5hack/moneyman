# with sql and without sql


import datetime


# dates
def date_today():
    x = datetime.date.today()
    print(x)
    print(x.year)
    print(x.strftime("%A"))
    print(x.strftime("%a"))


# date_today()

def date_made():
    x = datetime.datetime(2020, 12, 5)
    y = datetime.datetime(2020, 12, 10)
    print(x)
    print(x.strftime("%B"))

    z = x - y
    print(z)


# date_made()


def test1():
    amount = input("Enter amount: ")
    date_start = input("enter start date (yyyy, mm, dd): ")
    date_start = date_start.split(",")
    # print(date_duration)
    date_start = datetime.datetime(int(date_start[0]), int(date_start[1]), int(date_start[2]))

    date_start_year = date_start.year
    date_start_month = date_start.month
    date_start_day = date_start.month

    date_end = input("Enter end date (yyyy, mm, dd): ")
    date_end = date_end.split(",")
    date_end = datetime.datetime(int(date_end[0]), int(date_end[1]), int(date_end[2]))

    date_end_year = date_end.year
    date_end_month = date_end.month
    date_end_day = date_end.day

    if date_start_year == date_end_year:
        sum_months = date_start_month - date_end_month
        if sum_months < 0:
            sum_months = sum_months * -1

        total_amount_over_months = int(sum_months) * int(amount)
        print(total_amount_over_months)

    elif date_start != date_end_year:
        sum_year = date_start_year - date_end_year
        if sum_year < 0:
            sum_year = sum_year * -1

        additional_months = sum_year * 12

        sum_months = date_start_month - date_end_month
        if sum_months < 0:
            sum_months = sum_months * -1

        if sum_months == 0:
            sum_months = 1

        total_amount = int(sum_months) * int(amount) * int(additional_months)

        print(total_amount)


test1()


