from socket import *
import argparse
import threading
from datetime import datetime
import colorama
from colorama import Fore, Style

"""
A simple port scanner for scanning a list of
comma sperated ports on a domain. 

Usage:

python port_scan.py <host> <list-of-IP's>
"""
def check_port(host, port):
    try: 
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        print(f"{Fore.BLUE} [+] Port {port} is open")
    except (ConnectionRefusedError, timeout) as e :
        print(f"{Fore.RED} [-] Port {port} is closed")
    


def port_scan(host, ports):
    try:
        targetIP = gethostbyname(host) #get IP of the hostname
    except gaierror:
        print("Hostname Not known")

    threads = []
    setdefaulttimeout(10) 
    print(f"Scanning ports for {host} started at {datetime.now()}")
    
    for port in ports: 
        t = threading.Thread(
            target=check_port,
            args=(targetIP, int(port))
        )
        threads.append(t)
        t.start()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="print the status of ports of specified host")
    parser.add_argument("ports", help="check connection to the list of ports")

    args = parser.parse_args()

    host = args.host
    ports = args.ports
    ports = ports.split(',') # get the list of ports
    port_scan(host, ports)        

if __name__ == '__main__':
    main()