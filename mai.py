from datetime import datetime, timedelta, time
from datetime import date


def get_birthdays_per_week(users):
    # Дата сьогодні
    today = date.today()
    print(today)
    # Сьогоднійшній день тижня
    current_day_of_week = today.weekday()
    print(current_day_of_week)
    # Кількість днів до понеділку
    days_until_next_monday = (7 - current_day_of_week) % 7
    # Дата наступного понеділка
    time_difference = timedelta(days=days_until_next_monday)
    print(time_difference.days)
    next_monday = today + time_difference
    print(next_monday)
    # Дата наступної неділі
    next_sunday = next_monday + timedelta(days=6)
    print(next_sunday)
    # Список іменників цієї неділі
    users_to_greet = []


#     print("Next Monday:", next_monday)
#     print("Next Sunday:", next_sunday)

#     for user in users:
#         time_obj = time()
#         dt_next_monday = datetime.combine(next_monday, time_obj)
#         dt_next_sunday = datetime.combine(next_sunday, time_obj)
#         print("Next dtMonday:", dt_next_monday)
#         print("Next dtSunday:", dt_next_sunday)
#         print(user["birthday"])
#         if dt_next_monday <= user["birthday"].replace(year=2023) <= dt_next_sunday:
#             users_to_greet.append(user["name"])
#         print(users_to_greet)

#     # Виводимо спискок іменників по дням тижня
#     for i in range(7):
#         day = next_monday + timedelta(days=i)
#         day_name = day.strftime("%A")
#         day_users = []
#         for user in users:
#             user_birth_day = user["birthday"].strftime("%Y-%m-%d")
#             use = datetime.strptime(user_birth_day, "%Y-%m-%d").date()
#             if use == day_name:
#                 day_users.add(user["name"])
#                 print(day_users)
#         # print(f"{day_name}: {', '.join(day_users)}")
#         # if day_users:
#         #     print(f"{day_name}: {', '.join(day_users)}")


# спсок всіх іменників
# if __name__ == "__main__":
users = [
    {"name": "Bill", "birthday": datetime(1990, 10, 1)},
    {"name": "Jill", "birthday": datetime(1985, 10, 3)},
    {"name": "Kim", "birthday": datetime(1982, 10, 4)},
    {"name": "Jan", "birthday": datetime(1992, 10, 3)},
]

get_birthdays_per_week(users)
# print(1900, 10, 1)
