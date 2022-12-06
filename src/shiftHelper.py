import calendar
from datetime import datetime
from datetime import timedelta


def isValid(start, end):
    if start > end:
        return 'Start time happens after end time'

    if start.day != end.day or start.month != end.month or start.year != end.year:
        return 'Shift goes over multiple days'

    return 'All Good!'


def convertToDateTime(string):
    try:
        return datetime.strptime(string, '%Y-%m-%dT%H:%M')
    except:
        try:
            return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S')
        except: 
            return None

def weekShiftList(shifts, week):
    weekShifts = [[]] * 7
    dayShifts = []
    shiftIndex = 0
    day = convertToDateTime(week['min'])
    for i in range(7):
        if len(shifts) <= shiftIndex:
            break
        shift = shifts[shiftIndex]
        while day.day == shift.start.day and day.month == shift.start.month and day.year == shift.start.year:
            dayShifts.append({'id': shift.id, 'user_id': shift.user_id, 'start': shift.start, 'end': shift.end})
            shiftIndex += 1
            if len(shifts) <= shiftIndex:
                break
            shift = shifts[shiftIndex]
        
        weekShifts[i] = dayShifts
        dayShifts = []
        day = day + timedelta(1)

    return weekShifts

def validClockIn(shift):
    if shift.clockin != None:
        return False

    day = datetime.now() + timedelta(minutes=15)
    
    if (shift.start <= day and shift.end > day):
        return True
    else:
        return False

def canUserClockOut(shift):
    if shift.clockin is None:
        return False
    
    if shift.clockout is not None:
        return False
    
    return True

def removeShiftsNotInMonth(shifts):
    allShifts = []
    month = datetime.now().month

    for shift in shifts:
        if shift.start.month == month:
            allShifts.append(shift)
        else:
            break

    return allShifts

def getTotalHours(shifts):
    totalScheduled = 0
    totalHours = 0

    for shift in shifts:
        totalScheduled += (shift.end - shift.start).total_seconds() / 3600.0
        if shift.clockin is not None:
            if shift.clockout is None:
                totalHours += (shift.end - shift.clockin).total_seconds() / 3600.0
            else:
                totalHours += (shift.clockout - shift.clockin).total_seconds() / 3600.0


    return {'scheduled': round(totalScheduled, 2), 'hours': round(totalHours, 2)}


def organizeShifts(shifts, year, month):
    monthShifts = [''] * (calendar.monthrange(year, month)[1] + 1)

    for shift in shifts:
        if shift.start.month == month and shift.start.year == year:
            shiftText = shift.start.strftime("%H:%M") + "-" + shift.end.strftime("%H:%M")
            monthShifts[shift.start.day] = shiftText
        elif shift.start.month > month or shift.start.year > year:
            break

    return monthShifts
