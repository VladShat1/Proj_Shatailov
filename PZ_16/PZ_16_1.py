# Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
# методы для определения дня недели, проверки на високосный год и определения
# количества дней в месяце

import datetime
class Callendar:
    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d

    def find_day_of_week(self):
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        date_obj = datetime.date(self.y, self.m, self.d)
        week_day_num = date_obj.weekday()
        return week_days[week_day_num]

    def is_leap_year(self):
        if (self.y % 4 == 0 and self.y % 100 != 0) or self.y % 400 == 0:
            return True
        else:
            return False

    def days_in_month(self):
        if self.m in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.m in [4, 6, 9, 11]:
            return 30
        else:
            if self.is_leap_year():
                return 29
            else:
                return 28
