import calendar
from datetime import datetime
from datetime import timedelta


def isValid(start, end):
    if start > end:
        return 'Start time happens after end time'
    
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
    print(shifts)
    weekShifts = [[]] * 7
    dayShifts = []
    shiftIndex = 0
    for i in range(len(week)):
        shift = shifts[shiftIndex]
        while week[i] == shift.start.day:
            dayShifts.append({'id': shift.id, 'user_id': shift.user_id, 'start': shift.start, 'end': shift.end})
            shiftIndex += 1
            if len(shifts) <= shiftIndex:
                break
            shift = shifts[shiftIndex]
        
        weekShifts[i] = dayShifts
        dayShifts = []

    return weekShifts

def validClockIn(shift):
    day = datetime.now() + timedelta(minutes=15)
    if (shift.start <= day and shift.end > day):
        return True
    else:
        return False

def canUserClockOut(shift):
    if shift.start is None:
        return False
    
    if shift.end is not None:
        return False
    
    return True


def organizeShifts(shifts, year, month):
    print(shifts)

    monthShifts = [''] * (calendar.monthrange(year, month)[1] + 1)

    for shift in shifts:
        print(shift)
        if shift.start.month == month and shift.start.year == year:
            shiftText = shift.start.strftime("%H:%M") + "-" + shift.end.strftime("%H:%M")
            print(shift.start.day)
            monthShifts[shift.start.day] = shiftText
        elif shift.start.month > month or shift.start.year > year:
            break

    return monthShifts
