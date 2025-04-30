# Vikranth Pydeti                              02-22-2025
# Lab 5 - This code help find if the given year is a leap year or not.

def findLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def main():
    year = int(input("Please the year that you want to check if it is a leap year or no : "))
    answer = findLeapYear(year)

    if answer:
        print("YES, it is a leap year!")
    else:
        print("NO, It is not a leap year!")

if __name__ == "__main__" :
    main()