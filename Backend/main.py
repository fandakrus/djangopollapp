import socket
import sys
import json
from datetime import datetime
from time import sleep
from multiprocessing import Process
from threading import Thread
from queue import Queue


class Meassurement():

    def __init__(self) -> None:
        # queue used for data switching between threads
        self.queue = Queue()
        # port used for this comunication is 12345
        self.port = 12345
        # make new socket used to listen to values from measurments
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this binds socket to given port
        self.m_socket.bind(('', self.port))
        # let socket listen and que up max 5 connections
        self.m_socket.listen(5)        


    def listen(self):
        # keep listening for the incoming traffic and hendle the connections
        while True:
            c, addr = self.m_socket.accept()
            self.rcvData = c.recv(1024)
            # activate when message is recieved
            if self.rcvData is not None:
                self.results = json.loads(self.rcvData.decode('utf-8'))
                print(self.results)
                # append the recieved unjsoned message to the queue
                self.queue.put(self.results)
                self.rcvData = None
                self.results = None
                c.close()


    def pawel(self):
        print('pawel')
        sleep(4)

    
    def handle_queue(self):
        while not self.queue.empty():
            message = self.queue.get()
            print(message['humidity'], '     ze fronty')


def control(results):
    now = datetime.now()
    if now.hour < 4:
        return False, False
    # take care of all logic needed for the watering
    if results['tank'] > 500 and results['humidity'] < 500:
        return True, True
    elif results['humidity'] < 200:
        return True, False
    else:
        return False, False


def trigger(water, tank):
    # send data to second esp and trigger needed controls
    pass
        
def main():
    # creates new measurement unit
    meas = Meassurement()
    proc = Thread(target=meas.listen, args=())
    # let socket listen while other things happen
    proc.start()
    
    while True:
        meas.pawel()
        meas.handle_queue()


main()
"""
# make new socket used to listen to values from measurments
measure_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# port used for this comunication is 12345
port = 12345
# this binds socket to given port
measure_socket.bind(('', port))
# let socket listen and que up max 5 connections
measure_socket.listen(5)

# main running circle doing everything
while True:
    # get data about the sending host
    c, addr = measure_socket.accept()
    rcvData = c.recv(1024)
    if rcvData is not None:
        results = json.loads(rcvData)
        print(results['humidity'])
        c.close()
        water, tank = control(results)
        if water or tank:
            trigger(water, tank)
"""



    