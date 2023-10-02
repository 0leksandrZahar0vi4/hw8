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
        # створюємо список іменників

        user_celeb = []
        if (date_bd) in list(period):
            bd = bd.replace(year=start_day.year)
            print(bd)
            print(user["name"] + " імя іменинника")
            us = user["birthday"].strftime("%Y-%m-%d")
            user_day = (
                datetime.strptime(us, "%Y-%m-%d").date().replace(year=start_day.year)
            )
            # print(user_day, " дата народження іменинника")  # дата - тип
            user_celeb.append(user_day)
        print(user_celeb)
        days_until_next_monday = timedelta((7 - user_day.weekday()) % 7)
        # print(days_until_next_monday, " днів до понеділка")
        # знаходимо, в кого припадає ДН на вихідні і переносимо на понеділок
        users = {}
        if user_day.weekday() == 5 or user_day.weekday() == 6:
            use_celeb = days_until_next_monday + user_day
            # print(use_celeb)
            users[user["name"]] = user_day
        print(users)
        # шукаємо тих, хто вже святкував ДН
        userss_day = {}

        if (start_day - user_day).days < 0:
            users_day = user_day.replace(
                year=start_day.year + 1,
                month=user["birthday"].month,
                day=user["birthday"].day,
            )
            userss_day[user["name"]] = users_day
        print(userss_day)
        # якщо передаємо пустий список
        res1 = {}
        if (date_bd) not in list(period):
            print(res1)


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(1990, 10, 3)},
        {"name": "Jill", "birthday": datetime(2000, 10, 2)},
        {"name": "Kim", "birthday": datetime(1982, 10, 8)},
        {"name": "Jan", "birthday": datetime(1992, 7, 7)},
    ]
    get_bd(users)
    get_period(date(2023, 12, 29), 7)
