# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()


import network
ap = network.WLAN(network.AP_IF)                        # create access-point interface
ap.active(True)                                         # activate the interface
ap.config(essid='TempIR', password='87654321')          # set the ESSID of the access point


while ap.active() == False:
  pass