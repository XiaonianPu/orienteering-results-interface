import os
import sys
from SerialThread import SerialThread
from serial.tools import list_ports

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PACKAGE_DIR = SCRIPT_DIR + '/..'
sys.path.append(PACKAGE_DIR)

if __name__ == "__main__":
    port_list = list_ports.comports()
    print("Available port:")
    for index, port in enumerate(port_list):
        print("[{0}] {1} - {2}".format(index+1, port.name, port.description))
    station = input("Input Station COM name:")
    printer = input("Input Printer COM name:")
    thread1 = SerialThread(station, printer)
    thread1.start()