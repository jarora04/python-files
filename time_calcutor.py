import time
timespan=time.strftime('%H:%M:%S')
print(timespan)
timespan=time.strftime('%H')
print(timespan)
timespan=time.strftime('%M')
print(timespan)
timespan=time.strftime('%S')
print(timespan)
#strftime displays the time string into hours ,minutes and seconds format


if int(time.strftime('%H'))>=12 and int(time.strftime('%H'))<18:
    print("Good evening")
    
elif int(time.strftime('%H'))>=0 and int(time.strftime('%H'))<12:
    print("Good Morning")     
else:
    print("Good Night")