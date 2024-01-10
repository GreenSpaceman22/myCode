#!/usr/bin/env python3

def main():
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
    print(switch)
    print(type(switch))

    print( switch["hostname"] )
    print( switch["ip"] )

    print("First test - .get()")
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE"))

    print( "Third test - .get()")
    print(switch.get("version"))

main()
