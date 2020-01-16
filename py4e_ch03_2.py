#3.1 Write a program to prompt the user for hours and rate per
#hour using input to compute gross pay. Pay the hourly rate for
#the hours up to 40 and 1.5 times the hourly rate for all hours
#worked above 40 hours. Use 45 hours and a rate of 10.50 per hour
#to test the program (the pay should be 498.75). You should use
#input to read a string and float() to convert the string to a
#number. Do not worry about error checking the user input -
#assume the user types numbers properly.
try:
    hours = float(input("How many hours did you work?\n"))
    rate = float(input("What is your rate per hour?\n"))
except:
    print("Please input your information in the correct format")
    quit()

if 0 < hours <= 40:
    print(hours*rate)
elif hours > 40:
    reg_pay = 40*rate
    overtime = (hours - 40) * (1.5 * rate)
    print(reg_pay + overtime)
else:
    print("You have no payable hours on file.")
