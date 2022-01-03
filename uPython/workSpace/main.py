try:
  import usocket as socket 
except:
  import socket
import json
from time import sleep
  
  
def measurement():
  # this should measure all the neede values and return dict
  results = {'humidity': 5, 'pawel': 'kabel'}
  return results
  
def send(jdata):
  # get json so it can sand it to the server
  try:
    server = socket.socket()
  # creates socket and connect to the given ip need to be changed
    server.connect(('192.168.0.148', 12345))
  except:
    # server fail to connect this will try to close the socket and connect again
    server.close()
    server = socket.socket()
    server.connect(('192.168.0.148', 12345))

    
  server.sendall(jdata.encode('utf-8'))
  print('json sended')
  server.close()
  
while True:
  results = measurement()
  data = json.dumps(results)
  send(data)
  sleep(10)



