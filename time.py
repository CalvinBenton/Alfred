t = time.localtime()
localtime = time.strftime("%H:%M", t)
stringTime = "16:59"

if int(localtime[0:2]) > int(stringTime[0:2]):
	secondsToMidnight = (24 - int(localtime[0:2]))*60*60 + (0 - int(localtime[3:5]))*60
	hours = int(stringTime[0:2])
	mins = int(stringTime[3:5])
	seconds = hours*60*60 + mins*60 + secondsToMidnight
	print seconds

else:
	hours = int(stringTime[0:2]) - int(localtime[0:2])
	mins = int(stringTime[3:5])  - int(localtime[3:5])
	seconds = hours*60*60 + mins*60
	print seconds