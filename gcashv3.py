import uiautomator2 as u2
import json
import time
import gspread
from datetime import date
import os
from colorama import Fore
from os import system
system("title " + "GCASH AUTOMATED")
os.system('cls')
print(Fore.RED + "█" + Fore.WHITE + "GCASH BOT RUNNING...")
print("")
d = u2.connect('RFCT20CAK1E')
gc = gspread.service_account()
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1UbV7Tu3FdxtldKdplRNPtkg7MxpTkZj-HnDzN__Y3YM/edit?gid=0#gid=0')
sht = sh.worksheet("rec")
last_row = len(sht.get_all_values()) + 1
while True:
    i = 0
    if str(d(resourceId="com.android.systemui:id/quickcontrol_title").exists) == "False":
        d.swipe(38, 0, 38, 2000, steps=10)
    while i < d(resourceId="com.android.systemui:id/expandableNotificationRow").count:
        if d(resourceId="com.android.systemui:id/expandableNotificationRow")[i].child(resourceId="android:id/title").exists:
            rawnotif = json.dumps(d(resourceId="com.android.systemui:id/expandableNotificationRow")[i].child(resourceId="android:id/title").info)
            notif = json.loads(rawnotif)
            if(notif["text"] == "You have received money in GCash!"):
                rawnotif1 = json.dumps(d(resourceId="com.android.systemui:id/expandableNotificationRow")[i].child(resourceId="android:id/time").info)
                notif1 = json.loads(rawnotif1)
                rawnotif2 = json.dumps(d(resourceId="com.android.systemui:id/expandableNotificationRow")[i].child(resourceId="android:id/text").info)
                notif2 = json.loads(rawnotif2)
                print(Fore.GREEN + "▌" + Fore.WHITE + notif1["text"] + " " + notif2["text"]);
                print("")
                nrow = "A"+str(last_row)+":"+"C"+str(last_row)
                ntoday = str(date.today())
                sht.update([[ntoday,notif1["text"],notif2["text"]]], nrow)
                last_row += 1
                nx = notif2["visibleBounds"]
                nxc = json.dumps(nx)
                nnc = json.loads(nxc)
                nb = nnc["bottom"]
                nt = nnc["top"]
                nsx = ((nb - nt)/2)+nt
                d.swipe(204, nsx, 800, nsx, steps=10)
                i += d(resourceId="com.android.systemui:id/expandableNotificationRow").count
        i += 1
    sht2 = sh.worksheet("PAYMENT")
    sht2.update([["ONLINE"]], "D3")
    time.sleep(5)