import calendar
import datetime

#gets the current month, year, and calendar of the month
def getCurMonth():
    weekday = datetime.date.today().replace(day=1).weekday()
    daysinMonth = calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]

    cal = generateCal(weekday, daysinMonth)
    year = datetime.date.today().year
    month = datetime.datetime.now().strftime('%B')

    return {'month': month, 'year': year, 'cal': cal}

#generates the calendar in a format that is readable by the html
def generateCal(weekday, daysInMonth):
    weekday += 1
    if weekday == 7:
        weekday = 0

    month = []
    week = [''] * 7
    day = 1
    for i in range(daysInMonth):
        week[weekday] = day
        day += 1
        weekday += 1
        if weekday == 7:
            week = ['' if i is None else i for i in week]
            month.append(week)
            week = [None] * 7
            weekday = 0

    if any(week) is not None:   
        week = ['' if i is None else i for i in week]
        month.append(week)

    return month
