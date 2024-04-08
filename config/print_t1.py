"""
Print Label-Template#1 to QL810W
(c) 2024 by Dario Carluccio

Template stored at position #1 
in Brother QL 810W printer memory
has to accept one Parameter.

For more information goto:
https://github.com/dcbo/homeassistant-frosterlabels

Usage:
  python3 print_t1.py -t "TEXT"
  e.g.:
  python3 print_t1.py -t "Welcome Home"
"""
import socket
import argparse

def send_message(text):
    # IP-Address and Port of Printer
    host = '203.0.113.80'        
    port = 9100
    # print Template#1, and insert the only parameter
    message = "^II^TS001" + text + "^FF\n"
    # open socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    # send string
    s.sendall(message.encode('iso-8859-1'))
    # close socket
    s.close()

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, help='Text')
args = parser.parse_args()

if args.t is None:
    print("ERROR: mandatory parameter Text missing.")
else:
    send_message(args.t)
