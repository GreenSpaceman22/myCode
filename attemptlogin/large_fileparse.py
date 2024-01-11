#!/usr/bin/python3

loginfail = 0
posts = 0


keystone_file = open("/home/student/myCode/attemptlogin/keystone.common.wsgi","r")

for line in keystone_file:

    if  "- - - - -] Authorization failed"in line:
        loginfail += 1
    elif "POST" in line:
        posts += 1

print("The number of failed log in attempts is: ", loginfail)
print("The number of successful POSTs is: ", posts)


keystone_file.close()


