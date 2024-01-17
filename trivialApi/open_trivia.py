#!/usr/bin/env python3

import requests

URL= "paste the trivia url here"

def main():

    data= requests.get(URL).json()
    

    question1 = input()

if __name__ == "__main__":
    main()

