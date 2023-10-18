def isleapyear(year):
  if(year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = int(input(" enter the year : "))

if isleapyear(year):
  print("{} is leapyear".format(year))
else:
  print("{} is not leapyear".format(year))