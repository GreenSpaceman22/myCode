#!/usr/bin/python3

import json


def main():
    with open("datacenter.json","r") as datacenter:
        datacenterstring = datacenter.read()


    print(datacenterstring)
    print(type(datacenterstring))
    print("\n The code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")

    datacenterencoded = json.loads(datacenterstring)

    print(type(datacenterencoded))

    print(datacenterencoded)

    print(datacenterencoded["row3"])

    print(datacenterencoded["row2"][1])

if __name__ == "__main__":
    main()


