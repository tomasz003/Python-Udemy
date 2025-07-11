import requests, os
from twilio.rest import Client

OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
API_KEY=os.environ.get("OWM_API_KEY")
parameters={
    "lat": 50.06,
    "lon": 19.94,
    "cnt": 4,
    "appid": API_KEY
}
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
responder_phone_number=os.environ.get("RESP_PHONE_NUM")
response=requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data=response.json()
condition_codes=[forecast["weather"][0]["id"] for forecast in weather_data["list"]]

if any(condition_codes)<600:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+14255374555',
        body="\nIt's going to rain today!\nBring an umbrella!",
        to=responder_phone_number
    )
    print(message.status)

print(f"Status code: {response.status_code}")
