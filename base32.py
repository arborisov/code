import socket
import base64


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("62.173.140.174", 10002))
get1 = connection.recv(16384).decode("utf-8", "ignore")
connection.send("start\n".encode('utf8'))

def codeby():
    x = 0
    while x < 50:
        res = connection.recv(8196).decode('utf8', 'ignore')
        with open("examp.le", "w") as f:
            f.write(res)
        with open("examp.le", "r") as f:
            lines = f.read()
        word = lines[-16:-6]
        fuck = 'thin 5 sec'
        if word == fuck:
            continue
        else:
            word32 = base64.b32encode(word.encode('ascii'))
            connection.send(word32+'\n'.encode('utf8'))
            print(word32)
        x += 1
    print(connection.recv(16384).decode("utf-8", "ignore"))
codeby()
connection.close()
