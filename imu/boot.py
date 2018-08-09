import gc
import network
import machine
from machine import Pin

gc.collect()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
#sta_if.connect('ASK', 'qwertyuiop')
sta_if.connect('BSNL_AP', '12345678')
# ap_if.config(essid='ASK', password='qwertyuiop')
ap_if.active(False)
