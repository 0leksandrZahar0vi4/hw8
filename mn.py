from datetime import datetime, timedelta
from datetime import date


def get_period(start_day: date, days: int):
    res = {}
    for _ in range(days + 1):
        res[start_day.day, start_day.month] = start_day.year
        start_day += timedelta(1)
    return res


def get_bd(users):
    start_day = date.today()
    period = get_period(start_day, 7)
    end_period = start_day + timedelta(7)
    # print(end_period)

    for user in users:
        bd: date = user["birthday"]
        bd = bd.replace(year=start_day.year)
        date_bd = bd.day, bd.month
        if (date_bd) in list(period):
            bd = bd.replace(year=start_day.year)
            print(user["name"] + " імя іменинника")
            us = user["birthday"].strftime("%Y-%m-%d")
            use = datetime.strptime(us, "%Y-%m-%d").date().replace(year=start_day.year)
            print(use, " дата народження іменинника")
        dd = bd.weekday()
        print(bd.day, " день тижня народження")
        days_until_next_monday = (7 - dd) % 7
        print(days_until_next_monday)
        # if use.weekday() == 5 or use.weekday() == 6:
        #     use_celeb = date(year=2023, month=9, day=days_until_next_monday).weekday()
        #     use_celeb.strptime("%Y-%m-%d")
        #     print(use_celeb)
        # # print(type(use_celeb))
        # use_day = use.strftime("%A %d %B %Y")  # день в рядковому типі даних
        # print(use_day)

    res1 = {}
    if (date_bd) not in list(period):
        print(res1)


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(1990, 9, 30)},
        {"name": "Jill", "birthday": datetime(2000, 10, 1)},
        {"name": "Kim", "birthday": datetime(1982, 8, 30)},
        {"name": "Jan", "birthday": datetime(1992, 10, 3)},
    ]
    get_bd(users)
    # print(get_period(date(2023, 12, 29), 7))
