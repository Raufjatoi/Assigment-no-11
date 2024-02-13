from datetime import datetime 
date = 2024-2-14 # u can use input and make ur own date 
while True :
    if date == datetime.now().date():
        print('its ur day')
    else:
        print('its not ya day')
        break