# 2. Sleep Tracker: Create a program that asks the user for their 
# bedtime and wake-up time, then calculates their total sleep 
# duration. Use if statements to determine if they met the recommended sleep amount and 
# provide feedback accordingly
bedtime = input("Enter your bedtime (in HH:MM format): ")
wakeup_time = input("Enter your wakeup time (in HH:MM format): ")

bedtime_hour, bedtime_minute = map(int, bedtime.split(':'))
wakeup_hour, wakeup_minute = map(int, wakeup_time.split(':'))

bedtime_minutes = bedtime_hour * 60 + bedtime_minute
wakeup_minutes = wakeup_hour * 60 + wakeup_minute

sleep_duration_minutes = wakeup_minutes - bedtime_minutes
recommended_min_sleep = 7 * 60
recommended_max_sleep = 9 * 60

print("Your total sleep duration is:", sleep_duration_minutes // 60, "hours and", sleep_duration_minutes % 60, "minutes.")

if sleep_duration_minutes >= recommended_min_sleep and sleep_duration_minutes <= recommended_max_sleep:
    print("You met the recommended sleep duration. Well done!")
elif sleep_duration_minutes < recommended_min_sleep:
    print("You didn't get enough sleep. Aim for at least 7 hours.")
else:
    print("You overslept. Try to regulate your sleep schedule for better health.")
