import time
import requests
import datetime
import re
#when given text returns as human voice
def voice(message):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)

    engine.say(message)
    engine.runAndWait()

#when give int (minutes) returns alarm in that many minutes
def timer(length):
    timerInSeconds = float(length*60)
    print "setting timer for ", str(length), " minutes"
    voice("setting timer for " + str(length) + " minutes")
    time.sleep(timerInSeconds)
    print "timer is up, timer is up!"
    voice("Timer is up, timer is up!")

#given request returns time in format hh:mm
def returntime():
    t = time.localtime()
    localtime = time.strftime("%H:%M", t)
    print "the time is ", localtime
    voice("the time is " + localtime)

#given request returns weather in string format the temperature is C and weather is D
def weather():
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Hamilton&APPID=7a3ae847ce939ab3d50db89759873d2e&units=metric").json()
    temperature =  r["main"]["temp"]
    sky = r["weather"][0]["description"]
    print "The temperature is: ", str(temperature), "The weather is: ", sky
    voice("The temperature is " + str(int(temperature)) + " degrees celsius" + ". The weather is " + sky)

#given time in format hh mm returns an alarm at that time assuming future as far as tomorrow
def alarm(alarmH, alarmM):
    t = time.localtime()
    localtime = time.strftime("%H:%M", t)

    if int(localtime[0:2]) > alarmH:
        secondsToMidnight = (24 - int(localtime[0:2]))*60*60 + (0 - int(localtime[3:5]))*60
        seconds = alarmH*60*60 + alarmM*60 + secondsToMidnight
        print "setting alarm for ", alarmH, ":", alarmM
        voice("setting alarm for " + str(alarmH) + ":" + str(alarmM))
        time.sleep(seconds)
        print "Time to wake up sleepy head"
        voice("Time to wake up sleepy head")

    else:
        hours = alarmH - int(localtime[0:2])
        mins = alarmM  - int(localtime[3:5])
        seconds = hours*60*60 + mins*60
        print "setting alarm for ", alarmH, ":", alarm
        voice("setting alarm for " + str(alarmH) + ":"+ str(alarmM))
        time.sleep(seconds)
        print "Time to wake up sleepy head"
        voice("Time to wake up sleepy head")
          
        