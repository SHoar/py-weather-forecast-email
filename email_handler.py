import getpass
import smtplib

def get_emails():
    emails = {}

    # open the list of email addresses and names to send emails to
    try:
        email_file = open('emails.txt', 'r') 
        for line in email_file:
            (email, name) =  line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails
    
def send_emails(emails, schedule, forecast):
    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = getpass.getpass('What is your password? ')
    from_email = input('What is the username of the GMail account the emails will be sent from? ')
    
    # login to SMTP server with username, password
    server.login(from_email, password)


    # Send the email (from, to, message)
    
    for to_email, name in emails.items():

        # declare the subject and message of the email body
        message = "Subject: The Weather Forecast for Today\n"
        message += 'Hi ' + name + '\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope you enjoy the day!'

        # using smtplib, send email from, to, with included message
        server.sendmail(from_email, to_email, message)
    
    # quit the TLS SMTP server
    server.quit