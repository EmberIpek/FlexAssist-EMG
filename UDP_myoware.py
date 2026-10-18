# Author: Ember Ipek
#
# UDP class for sending and receiving data.

import network
import socket
import ustruct
import utime

class UDP:
    
    def __init__(self, tx_sock=None, rx_sock=None,
                 tx_port=5005, rx_port=5006, udp_ip=None):
        self.tx_sock = tx_sock
        self.rx_sock = rx_sock
        self.udp_ip = udp_ip
        self.tx_port = tx_port
        self.rx_port = rx_port
        
        if(rx_sock is not None):
            rx_sock.bind(("0.0.0.0", 5006))
            rx_sock.setblocking(False)
    
    def connect_wifi(self):
        # connect to hotspot
        ssid = "SSID"
        password = "PASSWORD"
        timeout = 20
        self.wlan = network.WLAN(network.WLAN.IF_STA)
        self.wlan.active(True)
        self.wlan.connect(ssid, password)
        
        while not self.wlan.isconnected() and timeout > 0:
            utime.sleep(0.5)
            timeout -= 1
            
        if self.wlan.isconnected():
            print("Connected to Wi-Fi: ", self.wlan.ifconfig())
        
        return self.wlan

    # maintain wifi connection
    def maintain_wifi(self, wlan):
        if not self.wlan.isconnected():
            print("Wi-Fi lost, reconnecting...")
            self.wlan = self.connect_wifi()
        
        return self.wlan

    # packs data for transmission over UDP and appends checksum
    # > = big endian, f = float, i = signed int
    def pack_data(self, adc_data, time_sent):
        packet = ustruct.pack(">ii", adc_data, time_sent)
#         checksum = self.calc_checksum(packet)
#         packet += ustruct.pack(">H", checksum)
        
        return packet
    
    def send_data(self, packet):
        if self.wlan.isconnected():
            self.tx_sock.sendto(packet, (self.udp_ip, self.tx_port))