from time import sleep
from machine import UART

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

while True:
  uart.write('pawel uart')
  print('pawel print')
  sleep(5)
