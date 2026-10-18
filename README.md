# Technica 2026

### EMG-Controlled Assistive Device

### Demo

[![Watch the video](https://img.youtube.com/vi/SXFi_Bxvxfk/hqdefault.jpg)](https://www.youtube.com/watch?v=SXFi_Bxvxfk)

This device uses a MyoWear 2.0 EMG device to send analog data through an ADC and detect finger extension. A stepper motor assists the user in extending fingers using fishing line when the muscle is contracted.

#### Dependencies & Credits - This project utilizes the following open-source libraries: 

**ADS1256 Driver**: Written by [robert-hh](https://github.com/robert-hh/ADS1256-ADS1255).

### 4:45

Initial ADC data acquired. Send to PC and graph.

### 5:30

Passing deque into np.arange requires converting into np array first. Added time_sent to packing function on client side to calculate t axis on graph.

[![Watch the video](https://img.youtube.com/vi/w6XfoWX4p8k/hqdefault.jpg)](https://www.youtube.com/watch?v=w6XfoWX4p8k)

### 7:00

MID and END electrodes placed along distal flexor muscles. Reference electrode placed on wrist. Sensor data graphed in real time shows muscle activation but does not use full ADC range (~30k-32k). Lag when graphing data. Find optimal electrode placement.

### 10:00

Removed Y-axis scaling on real-time graph for better response time. Sensor uses 5V rail for more ADC range. Electrodes start losing conductivity over time. Motor tested, keep polling adc data while running motor.

### 12:00

Implemented motor control logic based on sensor readings from ADC.

[![Watch the video](https://img.youtube.com/vi/e6-fv6-x0gE/hqdefault.jpg)](https://www.youtube.com/watch?v=e6-fv6-x0gE)

## 10/18/2026

### 8:00

Used fishing line to pull finger straight. Must find way to attach motor to arm. Options: rubber bands, scrunchie, duct dape. Prevent fishing line from slipping off motor. Eventually 3D print custom fitted housing for motor attached to forearm.

### 10:00
Attached motor to wrist with zipties and a scrunchie. Replaced fishing line with rubber bands attached to wire looped through glove as movement mechanism. Added forward and backward buttons as safety mechanism to override sensor data.

[![Watch the video](https://img.youtube.com/vi/SXFi_Bxvxfk/hqdefault.jpg)](https://www.youtube.com/watch?v=SXFi_Bxvxfk)

