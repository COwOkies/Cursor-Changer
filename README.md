# Cursor-Changer
CursorChanger let you change your windows cursor depending of the active app.

----------------------
Install requirements :
pip install -r requirements.txt

You can change values manually from the config.ini file, or use the config.pyw file.

Program -> The Program you want to change the cursor for. 
(the config.pyw shows openned app and let you choose one of them)
Defaultcursorname -> Default cursor Name or Path 
Newcursorname = New cursor Name or Path, place your cursor in the folder (.cur)
Timesleep = Time between checks (default = 0.5)

YSK For TimeSleep :
smaller value -> cursor adapt faster but high CPU usage (good computer)
higher value -> cursor adapt slower but it'll use less CPU (bad computer)

-----------------------

CursorChanger scans oppened apps until It find the one you set in values.
It'll then register his PID (process ID).
Then it will get the PID of the active app (according to the Timesleep value)
If the appID of the active app is the same as the PID registered earlier, it changes the cursor.


This program was originally intended for the Cemu emulator but it should works with a lot of apps :)

Made By COwOkie#6114 - Discord
