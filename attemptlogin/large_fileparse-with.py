#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
get= 0
post= 0
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            address= line.split()[-1]
            print(f"Authorization failed IP Address is {address}")
        if "- - - - -] GET" in line:
            get+= 1
        if "- - - - -] POST" in line:
            post+= 1
print("The number of failed log in attempts is\n", loginfail)
print("The number of GET is\n", get)
print(f"The number of POST is {post}")

