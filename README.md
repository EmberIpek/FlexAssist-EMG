# Technica 2026 - Hackathon Winner

### EMG-Controlled Hand Flexion Assistive Device

### Demo

[![Watch the video](https://img.youtube.com/vi/SXFi_Bxvxfk/hqdefault.jpg)](https://www.youtube.com/watch?v=SXFi_Bxvxfk)

This device uses a MyoWear 2.0 EMG device to send analog data to a Pi Pico through an ADC and detect finger extension. A stepper motor assists the user in extending fingers using rubber bands attached to a glove when the muscle is contracted.

### Circuit Diagram

<img width="975" height="673" alt="image" src="https://github.com/user-attachments/assets/3aa404a8-60b1-485a-8cfb-6ba70923affb" />

Available at: [https://www.circuitlab.com/editor/#?id=nvnkb6n5dq7z]

#### Dependencies & Credits - This project utilizes the following open-source libraries: 

**ADS1256 Driver**: Written by [robert-hh](https://github.com/robert-hh/ADS1256-ADS1255).

## Inspiration
Having a friend with Duchenne muscular dystrophy (DMD) opened my eyes to the challenges that come with progressive muscle weakness. Even simple actions such as scratching an itch becomes difficult as muscle function declines. I wanted to explore how embedded systems and biosignal sensing could help restore usable function in limbs.

## What it does
FlexAssist uses electromyography (EMG) to detect muscle activity and trigger a motorized mechanism that assists with finger extension. The goal is to explore how a user's muscle signals can be translated into mechanical assistance for everyday tasks.

## How it was built
A MyoWare 2.0 EMG sensor captures muscle activity and provides an analog signal to a 24-bit ADC. The acquired samples are transmitted to a computer for real-time visualization. When muscle activation is detected, the system controls a stepper motor through a motor driver. The motor pulls a rubber band connected to a glove, assisting finger extension.

## Challenges
Obtaining a usable EMG signal required trial and error with electrode placement. I also had to work around the limitations of available materials to mount the motor near the wrist and develop a mechanism that could pull the fingers toward extension.

## Accomplishments
I successfully integrated muscle sensing, analog-to-digital conversion, wireless data transmission, real-time signal visualization, and motor control into one working prototype. Seeing muscle activity appear on the live graph and using that signal to trigger a physical motor response was satisfying.

## What I learned
I gained hands-on experience with EMG sensing, electrode placement, analog signal acquisition, ADC integration, wireless communication, and motor control. I also learned how much sensor placement and mechanical design affects the performance of an EMG device.

## What's next for FlexAssist EMG
I plan to 3D-print a dedicated motor housing and improve the mechanism that secures the rubber bands. I also plan to apply digital signal processing techniques to filter noise and extract more useful information from the EMG signal, with the goal of making motor activation more reliable and responsive.

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

