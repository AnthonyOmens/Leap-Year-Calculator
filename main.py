#Basic Leap year calculator with functions, dictionary and anticipation of future leap years!!

def leap_year(year):
  """Returns true if its a Leap Year, otherwise false"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year, month):
  """Returns the amount of days in month depening if there is a leap year"""
  days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if leap_year(year) == False:
    return days_in_month_list[month - 1]
    #you gotta do month - 1 to shift the month input
  else:
      days_in_month_list[1] = 29
      return days_in_month_list[month - 1]

days_to_month = {
  1:'January',
	2:'February',
	3:'March',
	4:'April',
	5:'May',
	6:'June',
	7:'July',
	8:'August',
	9:'September',
	10:'October',
	11:'November',
	12:'December'}
#lets go dictionaries!! maybe I can make days_in_month_list a dictionary in a dictionary in the future

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(f"In the year {year}, {days_to_month[month]} will have {days} days")