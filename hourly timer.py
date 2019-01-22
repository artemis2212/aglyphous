# for finding out when a timer will go off given the start time and
#length of the timer
hours = int(input("What is the current time?(to the nearest hour)"))
alarm = int(input("How long would you like your timer to be?"))
print("Current time:")
print(hours,"O'Clock")
print("Time till alarm goes off:")
print(alarm, "hours")
days=(alarm//24)
print(days, "days till alarm goes off")
final_time=(hours+alarm)-(days*24)
print("The alarm will go off at:")
if final_time<13:
    print (final_time,"AM")
if final_time>12:
    print (final_time-12,"PM")
