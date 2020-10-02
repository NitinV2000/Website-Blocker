import time
from datetime import datetime as dt

# First check with the temp host file then do it the original and change it in code also
# Run through cmd and run it as admin

# To run it in background, change the extension to .pyw and then run it.
# To verify it you can check it in your task manager.
# To stop it do end process in the task manager

# To run it as soon as u open your laptop then create a task in task Scheduler
# Change triggers to at start
# Action to start a program 
# Other conditions as per your wish

hosts_temp = "hosts"
#hosts_temp = "C:\Users\nitva\Blocker\hosts"
#hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1" # Redirects to this page
website_list = ["www.facebook.com","facebook.com"] # Currently using these websites

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19): # You can decide the working hours and update.
        print("Working hours...")                                                                                     # I have kept it from 8:00 to 19:00
        with open(hosts_temp,'r+') as file: #to read and write file
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines() # Read the form in terms of lines to make it easier and then place the pointer at last
            file.seek(0) # To place the pointer at start to start writing from beginning
            for line in content: # Remember we cannot remove anything from files but can append them
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # To prevent repeating of writing and remove everything after that
        print("Fun time...")
    time.sleep(5) # Checks every 5 seconds.