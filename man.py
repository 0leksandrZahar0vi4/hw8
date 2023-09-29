from datetime import datetime, date, timedelta


users = [
    {"name": "Bill", "birthday": datetime(1990, 10, 1)},
    {"name": "Jill", "birthday": datetime(1985, 10, 3)},
    {"name": "Kim", "birthday": datetime(1982, 10, 4)},
    {"name": "Jan", "birthday": datetime(2023, 9, 27)},
]
day = date(year=2023, month=9, day=22)
print(day.day)
# t = int(input("Enter t: "))
# print(date(year=2023, month=9, day=t))
dd = day.weekday()
print(dd)
days_until_next_monday = (7 - dd) % 7
print(days_until_next_monday)
days = day.day + days_until_next_monday
print(date(year=2023, month=9, day=days))
print(date(year=2023, month=9, day=days).weekday())
# ddd = day + days
# print(ddd)
# if t == 5:
#     print(True)
#     print(date(day.year, day.month, day=0))
# else:
#     print(date(day.year, day.month, t))
# # dayt = time()
# print(dayt)
# # print(datetime(2023, 9, 27).strftime("%Y-%m-%d"))
# for user in users:
#     # The code `us = user["birthday"].strftime("%Y-%m-%d")` is converting the `birthday` value of each
#     # user in the `users` list to a string representation in the format "YYYY-MM-DD".
#     us = user["birthday"].strftime("%Y-%m-%d")
#     print(type(us))
#     use = datetime.strptime(us, "%Y-%m-%d").date()
#     print(use)
#     if use == day:
#         print("True")
#     else:
#         print("No")
# print(type(user["birthday"]))
# for i in user:
# if user["birthday"] == day:
#     print(user["birthday"])
#     print("Yes")
# else:
#     print("No")
