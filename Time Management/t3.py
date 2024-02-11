# 3. Meeting Scheduler: Design a program that helps users find a common meeting time among a 
# group. Use if-else statements to check for available time slots in each user's calendar and 
# suggest suitable meeting times.

# Define the calendars of users
user_calendars = {
    "Alice": ["9:00", "10:00", "11:00", "14:00", "15:00"],
    "Bob": ["9:30", "10:30", "11:30", "14:30", "15:30"],
    "Charlie": ["10:00", "11:00", "12:00", "15:00", "16:00"]
}

# Initialize a list to store available meeting times
common_meeting_times = []

# Iterate through each hour from 9:00 to 16:00
for hour in range(9, 17):
    # Convert the hour to a string
    hour_str = str(hour) if hour >= 10 else "0" + str(hour)
    
    # Check if all users are available at this hour
    all_available = True
    for user_calendar in user_calendars.values():
        if hour_str + ":00" not in user_calendar:
            all_available = False
            break
    
    # If all users are available, add the hour to common meeting times
    if all_available:
        common_meeting_times.append(hour_str + ":00")

# Print the available meeting times
print("Common meeting times:")
for time_slot in common_meeting_times:
    print(time_slot)
