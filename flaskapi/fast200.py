import time 
import requests

URI = "http://localhost:2224/"

def main():

    begin = time.time()
    while True:
        r = requests.get(f"{URI}fast")

        if r.status_code != 200:
            end_time = time.time()
            breakif r.status_code != 200:
            end_time = time.time()
            break
        print(f"To reach the limit of /fast, it took {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
