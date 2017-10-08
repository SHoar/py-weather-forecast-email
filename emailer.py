
import schedules
import weather
import email_handler

def main():
    
    # introduce our variables from our modules
    emails = email_handler.get_emails()
    schedule = schedules.get_schedule()
    forecast =  weather.get_weather_forecast()

    # send the emails with schedule and forecast included.
    try:
        email_handler.send_emails(emails, schedule, forecast)

        print(str(len(emails))+' Emails were sent!')
    except:
        print('Something went wrong. Emails did not send.')

main()
