import requests

time_url = "http://date.jsontest.com"
IP_url = "http://ip.jsontest.com"
validate_url = "http://validate.jsontest.com/"

def main():

    resp = requests.get(time_url)

    my_time = resp.json()

    mytime = mytime["time"].replace(" ", "").replace(":", "-")

    resp = requests.get(IP_url)
    my_ip = resp.json()
    print(my_ip["ip"])

    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    resp = requests.post(VALIDURL, data=mydata)

    respjson = resp.json()

    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
