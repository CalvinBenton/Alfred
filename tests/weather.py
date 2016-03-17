import requests

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Hamilton&APPID=7a3ae847ce939ab3d50db89759873d2e&units=metric").json()
print "The temperature is: ", r["main"]["temp"]
print "The weather is: ", r["weather"][1]["description"]

#api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=7a3ae847ce939ab3d50db89759873d2e
#api.openweathermap.org/data/2.5/weather?q=Hamilton&APPID=7a3ae847ce939ab3d50db89759873d2e
