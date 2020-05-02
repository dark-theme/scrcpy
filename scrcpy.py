# scrcpy.py

import os

DIR = "C:/Users/j p/Desktop/scrcpy"
BITRATE = 1536
SIZE = 800
FPS = 30

IP = "192.168.1.237"
PORT = 5555

def run():
    c = get_menu()
    while(c != '4'):
        if(c == '1'):
            os.system(f"cmd /c adb connect {IP}:{PORT}")
            
        elif(c == '2'):
            os.system("cmd /c adb disconnect")
            
        elif(c == '3'):
            os.system(f"cmd /c scrcpy -b {BITRATE}K -m {SIZE} --max-fps {FPS}")

        c = get_menu()

    # disconnect before exit
    os.system("cmd /c adb disconnect")

def get_menu():
    print("""
    1. Connect ADB
    2. Disconnect ADB
    3. Run scrcpy
    4. Quit
    """)

    inputset = {'1', '2', '3', '4'}
    
    i = input()
    while(i not in inputset):
        print("Invalid input")
        i = input()

    return i

if __name__ == "__main__":
    run()
