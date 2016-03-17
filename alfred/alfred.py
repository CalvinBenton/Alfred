import speech_recognition as sr
import pyttsx
import time
import requests
import datetime
import re

awake = False

def handler(input):
    global awake
    print "awake: ", awake
    if "Alfred" in input or awake == True:
        awake = True
        if "timer" in input:
            try:
                num = [int(s) for s in input.split() if s.isdigit()]
                timer(num[0])
            except:
                voice("Sorry, I didn't catch that")
          
        elif "time" in input:
            returntime()
        elif "weather" in input:
            weather()
        elif "alarm" in input:
            try:
                num = [int(s) for s in re.findall(r'\b\d+\b', input)]
                alarm(num[0], num[1])
            except:
                voice("Sorry, I didn't catch that")
               
        else:
            voice("Sorry, can you say that again")
            
    else:
        pass


#when given text returns as human voice
def voice(message):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)

    engine.say(message)
    engine.runAndWait()

#when give int (minutes) returns alarm in that many minutes
def timer(length):
    global awake
    timerInSeconds = float(length*60)
    print "setting timer for ", str(length), " minutes"
    voice("setting timer for " + str(length) + " minutes")
    awake = False
    time.sleep(timerInSeconds)
    print "timer is up, timer is up!"
    voice("Timer is up, timer is up!")

#given request returns time in format hh:mm
def returntime():
    global awake
    awake = False
    t = time.localtime()
    localtime = time.strftime("%H:%M", t)
    print "the time is ", localtime
    voice("the time is " + localtime)

#given request returns weather in string format the temperature is C and weather is D
def weather():
    global awake
    awake = False
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Hamilton&APPID=7a3ae847ce939ab3d50db89759873d2e&units=metric").json()
    temperature =  r["main"]["temp"]
    sky = r["weather"][0]["description"]
    print "The temperature is: ", str(temperature), "The weather is: ", sky
    voice("The temperature is " + str(int(temperature)) + " degrees celsius" + ". The weather is " + sky)

#given time in format hh mm returns an alarm at that time assuming future as far as tomorrow
def alarm(alarmH, alarmM):
    global awake
    t = time.localtime()
    localtime = time.strftime("%H:%M", t)

    if int(localtime[0:2]) > alarmH:
        secondsToMidnight = (24 - int(localtime[0:2]))*60*60 + (0 - int(localtime[3:5]))*60
        seconds = alarmH*60*60 + alarmM*60 + secondsToMidnight
        print "setting alarm for ", alarmH, ":", alarmM
        voice("setting alarm for " + str(alarmH) + ":" + str(alarmM))
        awake = False
        time.sleep(seconds)
        print "Time to wake up sleepy head"
        voice("Time to wake up sleepy head")

    else:
        hours = alarmH - int(localtime[0:2])
        mins = alarmM  - int(localtime[3:5])
        seconds = hours*60*60 + mins*60
        print "setting alarm for ", alarmH, ":", alarm
        voice("setting alarm for " + str(alarmH) + ":"+ str(alarmM))
        awake = False
        time.sleep(seconds)
        print "Time to wake up sleepy head"
        voice("Time to wake up sleepy head")
          
        


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        input_words = recognizer.recognize_google(audio)
        print "Alfred though you said: ", input_words
        handler(input_words)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
r = sr.Recognizer()
m = sr.Microphone()
with m as source:

    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
for _ in range(50): time.sleep(1) # we're still listening even though the main thread is doing other things
#stop_listening()  calling this function requests that the background listener stop listening
while True: time.sleep(3)
