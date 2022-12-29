### Problem 19
### https://projecteuler.net/problem=19

from datetime import datetime
startTime = datetime.now()

monthLength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dayName = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def leapYear(year):   # checks if given year is leap year
    if (year%4)!=0:
        return False
    elif (year%100)!=0:
        return True
    elif (year%400)!=0:
        return False
    else:
        return True

def dateDay(startYear, endYear):
    weekday = 2
    day = 1
    month = 0
    year = startYear
    count = 0

    while year < endYear:
        if leapYear(year) == True:   # changes length of february if year is leap year
            monthLength[1] = 29
        else:
            monthLength[1] = 28
        
        if dayName[(weekday % 7)-1] == "Sunday" and day == 1:   # counts every first of month sunday
            count += 1

        if day == monthLength[month] and month == 11:   # resets month and day at start of new year
            year += 1
            month = 0
            day = 0
        elif day == monthLength[month]:   # resets day at start of new month
            month +=1
            day = 0

        weekday += 1
        day += 1

    return count
        
print(dateDay(1901, 2001))
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: 171     #
# Time: 0:00.041  #
# # # # # # # # # #
