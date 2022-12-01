from datetime import datetime


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
        