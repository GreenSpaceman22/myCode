import requests, redirect, jsonify
import datetime

URL= "http://api.open-notify.org/iss-now.json"

def main():
    
    resp= requests.get(URL).json

    lat= resp["iss_position"]["latitude"]
    lon= resp["iss_position"]["longitude"]
    time_stamp = resp["timestamp"]
    time_stamp = datetime.datatime.fromtimestamp(timestamp)

    print(f"Current position of the ISS is: Longitude: {lon} and Latitude: {lat}")

if __name__ == "__main__":
    main()
