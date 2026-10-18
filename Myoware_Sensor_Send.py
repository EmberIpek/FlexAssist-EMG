import machine
import utime
import network
import socket
import ustruct
from UDP_myoware import UDP
from ads1256 import ADS1256

UDP_IP = "172.20.10.3"
TX_PORT = 5005
RX_PORT = 5006

# sck = Machine.Pin(2, Pin.OUT, value=0)
# din = Machine.Pin(3, Pin.IN)
# dout = Machine.Pin(4, Pin.OUT, value=0)
cs = machine.Pin(5, machine.Pin.OUT, value=1)
drdy = machine.Pin(6, machine.Pin.IN)

# setup UDP
tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp = UDP(tx_sock=tx_sock, rx_sock=rx_sock, udp_ip=UDP_IP)
wlan = udp.connect_wifi()

# adc0 = ADS1256(sclk, din, dout, cs, drdy)
# adc0.read(0)
# ads.channel(0, 0, 8, rate=15000)
spi0 = machine.SPI(0, sck=2, mosi=3, miso=4, phase=1, polarity=0)
adc = ADS1256(spi0, cs, drdy)


while True:
    wlan = udp.maintain_wifi(wlan)
    
    adc_data = adc.read(0)
    time_sent = utime.ticks_ms()
    print("adc data: ", adc_data)
    packet = udp.pack_data(adc_data, time_sent)
    udp.send_data(packet)
    utime.sleep_ms(10)