import os
import subprocess
from os import path

def headers():
    print("  ---------------------------------  ")
    print("  [-] Welcome to ADB Shell Wifi [-]  ")
    print("  [-]    by Yusril Rapsanjani   [-]  ")
    print("  ---------------------------------  ")
    print("  1. Set ADB Path                    ")
    print("  2. Connect to Devices              ")
    print("  ---------------------------------  ")
    adbPath = readADBPath()
    if adbPath != "KOSONG":
        print("  ADB_Location={}  ".format(adbPath))
        print("  ---------------------------------  ")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def readADBPath():
    filename = "config.dat"
    if path.exists(filename):
        fileConfig = open(filename, "r")
        return fileConfig.read().replace("ADB_LOCATION=", "")
    else:
        return "KOSONG"

def setADBPath():
    print("  ---------------------------------  ")
    print("      SETTING ADB PATH LOCATION      ")
    print("  ---------------------------------  ")
    while True:
        path = input("  [*] Insert your adb location: ")
        
        if path:
            filename = "config.dat"
            fileConfig = open(filename, "w")
            fileConfig.write("ADB_LOCATION={}".format(path))
            fileConfig.close()
            print("  [OK] Successfully setting adb location")
            clearConsole()
            startChoose()
            break
        else:
            continue
        

def connectDevices():
    print("  ---------------------------------  ")
    print("        CONNECTING TO DEVICES        ")
    print("  ---------------------------------  ")
    while True:
        ipAddress = input("  [*] Insert your ip address: ")
        if ipAddress:
            adbPath = readADBPath()
            if adbPath:
                os.chdir(adbPath)
                proccess = subprocess.Popen("./adb tcpip 5555".split(" "), stdout=subprocess.PIPE).communicate()[0]
                print("  [*] {}".format(proccess.decode("utf-8")))
                proccess = subprocess.Popen("./adb connect {}:5555".format(ipAddress).split(" "), stdout=subprocess.PIPE).communicate()[0]
                
                if str('connected to') in proccess.decode("utf-8"):
                    print("  [OK] Successfully connected")
                else:
                    print("  [x] Failed to connected")
                break
        else:
            continue


def startChoose():
    clearConsole()
    headers()
    
    while True:
        #Gettting menu input
        menu = input("  [*] Choose your menu: ")
        if menu == "1":
            setADBPath()
            break
        elif menu == "2":
            connectDevices()
            break
        else:
            print("  [x] Please choose correct menu")
            continue

def main():
    startChoose()

if __name__ == "__main__":
    main()