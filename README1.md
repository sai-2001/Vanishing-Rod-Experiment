# REMOTE TRIGGERED LAB
**The motive of RTL is to setup a realtime physical lab, which can operated remotely through a dashboard. Dashboard provides a visual interface to the user to control the physiacl components. The dashboard consists a video that serves as a visual of real time laboratory to the user.**


### VANISHING ROD

This expirement illustrates that when a material of some refractive index is placed in another material of same refractive index, it results in vanishing of the first material. The following phenomenon can be presented using vanishing rod expirement. When the reflection and refraction of the first object that was placed into second is eliminated then the first material vanishes.

In this case the refractive index of oil and galss rod is same, due to which the glass rod disappers when dipped into the oil. As the refractive index of the glass rod and the water are different, the reflection and refraction can't be eleminated. Hence the glassrod doesn't disappers in the water.



## Table content
- [Requirments](#Requirments)
- [Important links](#important-links)
- [Working](#working)
- [Code Explanation](#code-explanation)
- [Imported Librares](#libraries-to-be-imported)
- [Pins declered for stepper_motor-1](#pin-declaration-for-stepper-motor-1)
- [Pins decleared for stepper_motor-2](#pin-declerations-for-stepper-motor-2
)


## Requirments
 
1.Raspberry pi -model 3B+

2.Stepper motors -(28BYJ-48)

3.Relay

4.Drives

5.Beakers

6.Glass Rods

7.Pi cam

8.Led

9.Adapter

## Important Links
 
 - [About Blynk ](https://docs.blynk.io/en/)

- [How to connect Raspberry pi and Blynk](https://docs.blynk.cc/#hardware-set-ups-raspberry-pi)

- [Examples ](https://github.com/vshymanskyy/blynk-library-python)

- [Manual Device Activation](https://docs.blynk.io/en/getting-started/activating-devices/manual-device-activation)




## Working
### About Blynk
Blynk is a iot  platform that allows you to quickly build interfaces for controlling and monitoring your hardware projects from your iOS and Android device


In Blynk we can create-[Virtual pins ](https://docs.blynk.io/en/blynk.edgent-firmware-api/virtual-pins) that allow as to control the sensor/actuators remotly.



In this Project we have used Virtual pin V1 to reel and dereel stepper motors 
and Virtual pin V2 to Turn ON and OFF the lights
### Hardware Working
Stepper motors are connected to Raspberry Pi via Drives *(Drives-A drive is the electronic device that controls the electrical energy sent to the motor)*

 LED is connected to Raspberry pi via Relay
*(Relay- It is electronic switch which is similar to normal switch.)*

When the Virtual Pin V1 is turned ON the stepper motors dereels, which make the glass rod move downwards (dip into the liquid) .When the Virtual Pin V1 is turned OFF stepper motor gets reel, which make the glass rod move upwards.

When the Virtual pin V2 is turned ON the leds gets ON.
When the Virtual pin v2 is turned OFF the leds gets OFF




## Code Explanation
### Libraries to be imported
```
import RPi.GPIO as GPIO
import BlynkLib
from time import sleep
import sys 
   
````
## Blynk Credintials
```

BLYNK_TEMPLETE_ID='########'

BLYNK_DEVICE_NAME='########'

BLYNK_AUTH='############'

blynk=BlynkLib.Blynk(BLYNK_AUTH)
```
- To know the blynk credentials [Please refer the link](https://docs.blynk.io/en/getting-started/activating-devices/manual-device-activation)

### Pin Declaration for Relay
```
rp = 18       # Declaration of rp (relay pin),  18 is GPIO pin of Raspberry pi

```





### Pin Declaration for stepper motor 1

```
m1 = (11,13,15,16)         ## 11,13,15,16 are GPIO pins of Raspberry pi
GPIO.setup(m1, GPIO.OUT)   ## GPIO.setup() sets the stepper motor1 pins as output pins 

```
### Pin Declerations for stepper motor 2
```
m2 = (29,31,33,35)        ## 29,31,33,35 are GPIO pins of Raspberry pi
GPIO.setup(m2, GPIO.OUT)  ## GPIO.setup() sets the stepper motor2 pins as output pins 
```
## Rod dipped into the liquid
```
def reel():
    print("reel") 
    b=0                                                             # Intalize the loop to start from Zero
    while b<950:                                                    # b is calibrated value which defines number of times the loop should be repeated, which results in effective reel.*

        GPIO.output(m1, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))     # GPIO.output() set one of the GPIO pin to High in a sequencial order, which results in defined rotation of stepper motor (i.e.clockwise or anti-clockwise)
        sleep(0.002)
        GPIO.output(m1, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m1, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m1, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m2, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.002)
        GPIO.output(m2, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m2, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m2, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        b+=1                                                        # for every instance b value is incremented 
```
### Stepper Motor Rotation
```

def dereel():
    print("Dereel")
    d=0 # Used to start the motor from low
    while d<950: # The No.of Rotations covered by motor which pulls the rod down
        GPIO.output(m1, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m1, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m1, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m1, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.002)
        GPIO.output(m2, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m2, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m2, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
        sleep(0.002)
        GPIO.output(m2, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.002)
        d+=1
```

### led ON
```

GPIO.setup(rp,GPIO.OUT)             #GPIO.setup() sets the relay pin as output pin
To set the LED ON
def relayon():                      # relayon() is used to turn on the light when device went online
     GPIO.output(rp,GPIO.HIGH)

```
### led OFF

```
def relayoff():                     # relayoff() is used to turn off the light 
     GPIO.output(rp,GPIO.HIGH)
```

## connecting to Blynk
```
@blynk.on("connected")              # @blynk.on() is used to connect to the blynk
def blynk_connected():
    print ("conected")
   
@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected') 
    blynk.connect()                 # Reconnect to Blynk when it is disconnected 
```
## Reading Virtual pin V1 
```
@blynk.on("V1")
def V1_write_handler(value):    # reads the value(state) of virtual pin V1
 val1= int(float(value[0]))     # val1 stores the value[0] i.e,LSB(Least significant bit) of value
    if val1 == 1:               # when val1==1 then the reel function executes.
        reel()
    elif val1 == 0:             # when val1==0 then the dereel function  executes.
        dereel()
```
## Reading Virtual pin V2 
```
@blynk.on("V2")
def V2_write_handler(value):   # reads the value of virtual pin  V2
    print(value[0])
    val2= int(float(value[0])) 
    if val2 == 1:               # when Val2==1 then the relayon function executes
        relayon() 
    elif val2 == 0:             # when Val2==0 then the relayoff function executes
        relayoff()  
```
### To run the Blynk

```
while True:
    blynk.run()               
```
