import calendar
import datetime
from datetime import date
from dateutil import relativedelta

#gets the current month, year, and calendar of the month
def getCurMonth():
    weekday = datetime.date.today().replace(day=1).weekday()
    daysinMonth = calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]

    cal = generateCal(weekday, daysinMonth)
    year = datetime.date.today().year
    month = datetime.datetime.now().strftime('%B')

    return {'month': month, 'year': year, 'cal': cal, 'next': False}

def getNextMonth():
    today = datetime.date.today()
    nextMonthDate = today + relativedelta.relativedelta(months=1, day=1)

    weekday = nextMonthDate.weekday()
    daysinMonth = calendar.monthrange(nextMonthDate.year, nextMonthDate.month)[1]

    cal = generateCal(weekday, daysinMonth)
    year = nextMonthDate.year
    month = nextMonthDate.strftime('%B')

    return {'month': month, 'year': year, 'cal': cal, 'next': True}

def getMonthAndYear():
    year = datetime.date.today().year
    month = datetime.datetime.now().strftime('%B')
    return {'month': month, 'year': year}

def getCurWeek():
    today = datetime.date.today()
    week = []
    d = today.toordinal()
    sunday = d - (d % 7)
    saturday = sunday + 6
    year = date.fromordinal(sunday).year
    month = date.fromordinal(sunday).strftime('%B')
    for i in range(7):
        week.append(date.fromordinal(sunday+i).day)

    return {'month': month, 'year': year, 'week': week, 'min': date.fromordinal(sunday).strftime("%Y-%m-%dT%H:%M:%S"), 'max': date.fromordinal(saturday).strftime("%Y-%m-%dT%H:%M:%S")}

def getCurWeekFromDay(day):
    week = []
    d = day.toordinal()
    sunday = d - (d % 7)
    saturday = sunday + 6
    year = date.fromordinal(sunday).year
    month = date.fromordinal(sunday).strftime('%B')
    for i in range(7):
        week.append(date.fromordinal(sunday+i).day)

    return {'month': month, 'year': year, 'week': week, 'min': date.fromordinal(sunday).strftime("%Y-%m-%dT%H:%M:%S"), 'max': date.fromordinal(saturday).strftime("%Y-%m-%dT%H:%M:%S")}

def getLastWeek(day):
    week = []
    d = day.toordinal()
    saturday = d-1
    sunday = saturday - 6
    year = date.fromordinal(sunday).year
    month = date.fromordinal(sunday).strftime('%B')
    for i in range(7):
        week.append(date.fromordinal(sunday+i).day)

    return {'month': month, 'year': year, 'week': week, 'min': date.fromordinal(sunday).strftime("%Y-%m-%dT%H:%M:%S"), 'max': date.fromordinal(saturday).strftime("%Y-%m-%dT%H:%M:%S")}

def getNextWeek(day):
    week = []
    d = day.toordinal()
    sunday = d+1
    saturday = sunday + 6
    year = date.fromordinal(sunday).year
    month = date.fromordinal(sunday).strftime('%B')
    for i in range(7):
        week.append(date.fromordinal(sunday+i).day)

    return {'month': month, 'year': year, 'week': week, 'min': date.fromordinal(sunday).strftime("%Y-%m-%dT%H:%M:%S"), 'max': date.fromordinal(saturday).strftime("%Y-%m-%dT%H:%M:%S")}


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
            month.append(week)
            week = [''] * 7
            weekday = 0

    if week[0] != '':   
        month.append(week)

    return month

