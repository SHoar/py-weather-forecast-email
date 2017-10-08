def get_schedule():
    
    # Open the file with the day's schedule    
    try:
        schedule_file = open('schedule.txt', 'r')
        schedules = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
        
    return schedules