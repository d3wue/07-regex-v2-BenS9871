import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here

IPv4 = re.compile("((2[0-5][0-5]|1[0-9][0-9]|[0-9][0-9]?)\.){3}(2[0-5][0-5]|1[0-9][0-9]|[0-9][0-9]?)")
m = IPv4.match("1.255.1.1")
print(m)

IPv6 = re.compile("(([0-9]|[a-f]){4}:){7}([0-9]|[a-f])")
m = IPv6.match("2001:0db8:0000:0000:0000:ff00:0042:8329")
print(m)
#warum schneidet das in der konsole unten immer ab der 8 ab?

IPv4_counter = 0
IPv6_counter = 0
wrong_IPs = 0

for ip in ipAddresses:
    if IPv4.match(ip):
        IPv4_counter += 1
    elif IPv6.match(ip):
        IPv6_counter += 1
    else:
        wrong_IPs += 1

print(f'IPv4: {IPv4_counter}')
print(f'IPv6: {IPv6_counter}')
print(f'Wrong IP: {wrong_IPs}')
