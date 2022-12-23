KEY = 'c4c262d37c005ded7291cf0659d6b01e'
daily = 'b6ea5ca4052d9551852631e82e0720a8'
import requests
import geocoder as g
import datetime

def get_weather():
    city = g.ip('me').city
    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric')
    data = req.json()
    city_name =  data['name']
    temp = round(int(data['main']['temp']))
    curr_temp = f"{temp} °C"
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    now = datetime.datetime.now() 
    day = datetime.datetime.weekday(now)
    days_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    week_day = days_list[day]
    icon = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    return {'city': city_name, 'temp': curr_temp, 'icon': icon, 'date': date, 'day': week_day}

# latlong = g.ip('me').latlng
# latit = latlong[0]
# longit = latlong[1]
# cnt = 7

# dailyreq = requests.get(
#     f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={latit}&lon={longit}&cnt={cnt}&appid={daily}&units=metric')
# pprint(dailyreq.json())

# get_weather()