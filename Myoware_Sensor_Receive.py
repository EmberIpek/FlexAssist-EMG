import socket
import struct
import time
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

UDP_IP = "0.0.0.0"
PICO_IP = "172.20.10.11"
TX_PORT = 5006
RX_PORT = 5005

def plot_spectrum(Xv, fs, doStem=False):
	"""Plot magnitude and phase of the spectrum"""

	N = len(Xv)
	ff = np.arange(-N/2, N/2, 1) * fs/N

	fig, (axm, axp) = plt.subplots(2, 1, layout='constrained')
	
	if doStem:
		axm.stem(ff, np.abs(Xv))
	else:
		axm.semilogy(ff, np.abs(Xv))
	axm.grid()
	axm.set_ylabel('Magnitude')

	if doStem:
		axp.stem(ff, np.angle(Xv)/np.pi)
	else:
		axp.plot(ff, np.angle(Xv)/np.pi)
	axp.set_xlabel('Frequency (Hz)')
	axp.set_ylabel('Phase (rad/pi)')
	axp.grid()

	plt.show()

# initialize UDP
tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx_sock.bind((UDP_IP, RX_PORT))
print("Listening on port", RX_PORT)

data_samples = deque(maxlen=500)
time_sent = deque(maxlen=500)
count = 0

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel("Time (s)")
ax.set_ylabel("ADC value")
ax.set_title("ADS1256 Live Data")
ax.grid(True)

while True:
    data, addr = rx_sock.recvfrom(1024)
    #print("Received", len(data), "bytes from", addr)
    
    # > = big endian, i = integer
    try:
        data = struct.unpack(">ii", data)
        adc_data = data[0]
        time_sent.append(data[1])
        print("UDP received! data: ", adc_data)
        data_samples.append(adc_data)
        count += 1
        
        # create real-time plot of ADC data
        if (count % 10 == 0):
            y = np.asarray(data_samples)
            ts = np.asarray(time_sent, dtype=np.int64)
            
            # Time relative to the newest sample, in seconds
            t = (ts - ts[-1]) / 1000.0
            line.set_data(t, y)
            ax.set_xlim(-5, 0)
            if len(y) > 1:
                ymin = np.min(y)
                ymax = np.max(y)
                margin = max((ymax - ymin) * 0.1, 1)
                ax.set_ylim(ymin  - margin, ymax + margin)
                
            fig.canvas.draw_idle()
            fig.canvas.flush_events()
            # plt.pause(0.001)
    except struct.error:
        print("Packet unpacking failed")
# finally:
#     rx_sock.close()
#     tx_sock.close()