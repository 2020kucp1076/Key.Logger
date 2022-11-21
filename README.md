# Key.Logger

Cool features:
1. Embeddable in a file like document, image ...etc.
2. Start with system startup automatically.
3. Send key strokes on your mail.
4. Looks like a legit file(Extension spoofing, Icon spoofing).
5. Runs in background quietly.

If you want to stop the program, find file location of "Windows_Explorer.exe" from startup programs( in task manager), delete it and restart your system.

Required things before running on any system:
1. Windows environment.
2. Disable antivirus real time scanning as AV evasion isn't implemented.
3. If there is any error coming after running it, try again with a home network or personal hotspot.

Please do follow all the steps if you want a cool correctly configured program.

You need four files in same folder to make a final keylogger file:
1. call_trojan.py
2. trojan.py
3. ".ico" file of your required icon image.
4. image for embedding.
( Install all python libraries imported in "trojan.py" file )

There are some changes you have to do before making a final packaged program:

![image](https://user-images.githubusercontent.com/75797944/203025462-ee396f25-276c-4349-8648-5ce14255a677.png)

Changes in above part of program:
1. Timer after which you will receive a mail containing key strokes, by default it's 300 sec(5 min). you can change it to meet your requirments. 
2. keylogger login into your mail account and send a mail to itself with key stokes. Enter a mail id on which you want to receive mails.
3. You have to enter a 3rd party app password of above mail if your mail service doesn't allow direct password login from 3rd party app. You can obtain it by following your mail service provider documentation.

if your mail service provides direct login from 3rd party app, you can go directly with your mail account password.

4. 



