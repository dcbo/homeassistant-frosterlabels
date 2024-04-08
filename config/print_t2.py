"""
Print Label-Template#2 to QL810W
(c) 2024 by Dario Carluccio

Template stored at position #1
in Brother QL 810W printer memory
has to accept three Parameters.

For more information goto:
https://github.com/dcbo/homeassistant-frosterlabels

Usage:
  python3 print_t2.py -p "PRODUCT" -m "AMMOUNT"
  e.g.:
  python3 print_t2.py -p "Hühnersuppe" -m "3 Liter"

"""
import socket
import argparse
from datetime import datetime

def send_message(produkt, menge):
    # IP-Address and Port of Printer
    host = '203.0.113.80'    
    port = 9100
    # compose date
    actual_date = datetime.now()
    formatted_date = actual_date.strftime("%d.%m.%Y")
    # print Template#2, and insert three parameters (-p, -m and the actual date)
    message = "^II^TS002" + produkt + "\t" + menge + "\t" + formatted_date + "^FF\n"
    # open socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    # send string
    s.sendall(message.encode('iso-8859-1'))
    # close socket
    s.close()

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str, help='Produkt')
parser.add_argument('-m', type=str, help='Menge')
args = parser.parse_args()

if args.p is None or args.m is None:
    print("ERROR: mandatory parameters 'Produkt' and 'Menge' missing.")
else:
    send_message(args.p, args.m)
