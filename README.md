# py-weather-forecast-email
This is a Python3 command-line app that will send the current weather forecast and the listed day's schedule to  a list of emails.

<u>Project Requirements</u>

You must have Python 3.4+ installed to run this application. The development test site used Python 3.6.3, but I believe that 3.4+ will be fine.

To clone this app, enter these commands:

<code>
  git clone https://github.com/SHoar/py-weather-forecast-email.git &&
  cd py-weather-forecast-email
</code>
<br/>
<br/>
This email smtp handler sends email with TLS encryption.  If you are using GMail to send your emails, you must either change your sender email account to 'allow less secure apps'
or use App Passwords, but this application repo is using the former method.

In order to use this applications, there are three required files you will need:
<ol>
  <li><strong>emails.txt</strong> - This file must list the emails that will be sent to, in order of <code> email_address , name </code> on each line.  This file has not been included, and you must create it on your own.</li> 
  <li><strong>schedule.txt</strong> - This file will have a list of events and times, with each line being one event. You may use the file included, but I suggest putting in your own real schedule.</li>
  <li><strong>secrets.py</strong> - This application utilizes the <a href='http://openweathermap.org/current' target='_blank'>OpenWeatherMaps Current Weather API</a>.  You will need to sign up for an API key, if you have not already done so, and use it as the APP_ID for the query string inside <code>weather.py</code></li>
</ol>

The application will ask you what city you want to look up.  Once the query is made, this city's weather will be sent to each email in the <code>emails.txt</code> file, along with the schedule that is in <code>schedule.txt</code>.

The command-line tool will ask you for your email password, but it uses the python library <code>getpass</code> to prompt the user, so the password will not be seen in the terminal as it is typed.

To run the program, there are a couple different ways to do it. If you like typing alot, type: <code>python3 emailer.py</code> and hit enter to run.

If you prefer shortcuts, I've created a Windows batch file (<code>weather.bat</code>), or <code>weather.sh</code> if you prefer bash/linux shell.

So, to execute--

On Windows:
<ol>
  <li>double-click <code>weather.bat</code> from the File Explorer, or run it from the commmand prompt in Powershell or the MS-DOS prompt.</li>
</ol>
On Linux/ MacOS:
<ol>
  <li>From the terminal, run <code>bash weather.sh</code> or <code>sh weather.sh</code></li>
</ol>

You should be confirmed with a count of how many emails have been sent when the process has finished.