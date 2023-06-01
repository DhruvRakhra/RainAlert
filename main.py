import requests
from twilio.rest import Client

account_sid = "AC09e9e746667534be0df5f758ce000784"
auth_token = "938312fa031d043b72df520a2ae454ae"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9f5ddbe67487430109c76f3b5fb3ff1d"

weather_prams = {
    "lat": 30.3165,
    "lon": 78.0322,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=weather_prams)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella☂",
                from_="+14344742562",
                to="+918572841355")
    print(message.status)
