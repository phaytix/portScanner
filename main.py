#!/usr/bin/python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

host = input("Please enter IP you want to scan:")
port = input("Please enter port you want to scan:")


def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("Port is open")

portScanner(port)