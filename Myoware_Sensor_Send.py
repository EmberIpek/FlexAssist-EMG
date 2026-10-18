# Author: Ember Ipek
# 10/17/2026
#
# Acquires data from MyoWear 2.0 EMG device through an ADC
# and uses stepper motor to assist in hand movement.

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
in1 = machine.Pin(13, machine.Pin.OUT, value=0)
in2 = machine.Pin(12, machine.Pin.OUT, value=0)
in3 = machine.Pin(11, machine.Pin.OUT, value=0)
in4 = machine.Pin(10, machine.Pin.OUT, value=0)
forward_button = machine.Pin(15, machine.Pin.IN, pull=machine.Pin.PULL_UP)
backward_button = machine.Pin(14, machine.Pin.IN, pull=machine.Pin.PULL_UP)

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
motor_count = 0
count = 0

def setStep(w1, w2, w3, w4):
    in1.value(w1)
    in2.value(w2)
    in3.value(w3)
    in4.value(w4)
    
    return

def motor_forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        utime.sleep_ms(delay)
        setStep(0, 1, 0, 0)
        utime.sleep_ms(delay)
        setStep(0, 0, 1, 0)
        utime.sleep_ms(delay)
        setStep(0, 0, 0, 1)
        utime.sleep_ms(delay)
        
    return

def motor_backward(delay, steps):
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        utime.sleep_ms(delay)
        setStep(0, 0, 1, 0)
        utime.sleep_ms(delay)
        setStep(0, 1, 0, 0)
        utime.sleep_ms(delay)
        setStep(1, 0, 0, 0)
        utime.sleep_ms(delay)
        
    return

def motor_stop():
    setStep(0, 0, 0, 0)
    
    return

while True:
#     wlan = udp.maintain_wifi(wlan)
#     
    adc_data = adc.read(0)
#     time_sent = utime.ticks_ms()
    print("adc data: ", adc_data)
#     packet = udp.pack_data(adc_data, time_sent)
#     udp.send_data(packet)
    
    if (forward_button.value() == 0):
        motor_forward(2, 1)
    elif (backward_button.value() == 0):
        motor_backward(2, 1)
    # use counter to make sure motor does not overextend
    elif (adc_data > 690000 and motor_count < 100):
        motor_forward(2, 10)
        motor_count += 1
    elif (motor_count > 0):
        motor_backward(2, 10)
        motor_count -= 1
    
    count += 1
#     if (count % 1000 == 0):
#         print(adc_data)c
    utime.sleep_ms(10)
