import re

ip = input("enter ip address: ")

ipv4 = r"^(\d{1,3}\.){3}\d{1,3}$"
ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

if re.match(ipv4,ip):
    parts = ip.split(".")
    valid = True
    for i in parts:
        if int(i) > 255:
            valid = False
    if valid:
        print("valid ip")
    else:
        print("invalid ip")
elif re.match(ipv6,ip):
    print("valid ip")
else:
    print("invalid ip")