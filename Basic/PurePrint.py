import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PACKAGE_DIR = SCRIPT_DIR + '/..'
sys.path.append(PACKAGE_DIR)

from SerialThread import SerialThread
from serial.tools import list_ports



if __name__ == "__main__":
    port_list = list_ports.comports()
    print("Available port:")
    for index, port in enumerate(port_list):
        print("[{0}] {1} - {2}".format(index, port.name, port.description))
    station = int(input("Input Station COM index:"))
    printer = int(input("Input Printer COM index:"))
    thread1 = SerialThread(port_list[station].device, port_list[printer].device)
    thread1.start()