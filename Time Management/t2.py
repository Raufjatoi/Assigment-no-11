# 2. Pomodoro Timer: Create a program that implements the Pomodoro Technique (25 minutes 
# work, 5 minutes break). Use a loop and if statements to track time intervals and notify the user 
# when to switch between work and breaks.
import time

WORK_DURATION = 25 * 60  # 25 minutes in seconds
BREAK_DURATION = 5 * 60   # 5 minutes in seconds

while True:
    # Work period
    print("Work for 25 minutes.")
    time.sleep(WORK_DURATION)

    # Break period
    print("Take a 5-minute break.")
    time.sleep(BREAK_DURATION)
