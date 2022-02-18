from goto import *
import time
import var
import pio
import resource
import Ports

def peripheral_setup():
    pio.terminal = Ports.SerialTerminal(9600)

def variable_setup():
    var.Name = ''

def peripheral_loop():
    pass

def main():
    peripheral_setup()
    pio.terminal.println('Whats your name?')
    var.Name = pio.terminal.input(True)
    while var.Name != 'thay Thao dep giai':
        pio.terminal.println('Sai ten roi  mike pence')
        var.Name = pio.terminal.input(True)
    pio.terminal.println("Hello " + var.Name)
    while 1:
        peripheral_loop()
