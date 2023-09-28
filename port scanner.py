import socket, threading

from bs4 import BeautifulSoup


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''


def scan_ports(host_ip, delay):
    threads = []
    output = {}

    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)
    for i in range(10000):
        threads[i].start()
    for i in range(10000):
        threads[i].join()
    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ':' + output[i])


def main():
    from bs4 import BeautifulSoup


import requests

url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
