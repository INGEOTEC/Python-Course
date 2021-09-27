# doy = int(input("Enter the day of the year: "))
doy = 366

days = [31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

flag = True
for i in range(12):
    if flag and doy <= 0:
        print("Enter a positive integer")
        flag = False
    if flag and doy <= days[i]:
        print(months[i], doy)
        flag = False
    doy = doy - days[i]
if flag:
    print("There are only 365 days in a year")