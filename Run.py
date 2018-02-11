import string
from Read import getUser, getMessage
from Socket import openSocket
from Initialize import joinRoom
from Socket import sendMessage

s = openSocket ()
joinRoom(s)
readbuffer=""

while True:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            if "PING" in line:
                    s.send(line.replace("PING", "PONG"))
                    break
            user = getUser(line)
            message = getMessage(line)
            print user + " typed:" + message
            if "pickles" in message:
                sendMessage(s,"I like Pickles!")


