with open("dnsservers.txt", "r") as dnsfile:
    for svr  in dnsfile:
        print(svr, end="")

