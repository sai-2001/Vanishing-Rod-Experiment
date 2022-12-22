

import RPi.GPIO as GPIO
import BlynkLib
from time import sleep
import sys
## Blynk Credintials

BLYNK_TEMPLETE_ID='-------'        # Place your Blynk templete id
BLYNK_DEVICE_NAME='---------'      # Place your Device name
BLYNK_AUTH='------------'          # Place your Authentication Token here
blynk=BlynkLib.Blynk(BLYNK_AUTH)
rp = 18 # Declared a pin for relay

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
m1 = (11,13,15,16) 					#11,13,15,16 are GPIO pins of Raspberry pi
m2 = (29,31,33,35) 					#29,31,33,35 are GPIO pins of Raspberry pi
GPIO.setup(m1, GPIO.OUT)  			# GPIO.setup() sets the stepper motor1 pins as output pins 
GPIO.setup(m2, GPIO.OUT)  			# GPIO.setup() sets the stepper motor2 pins as output pins 
GPIO.setup(rp,GPIO.OUT)

# Rod dipped into the liquid
def reel():
    print("reel")
    b=0 							                                        # Intalize the loop to start from Zero

    while b<950: 						                                    # b is calibrated value which defines number of times the loop should be repeated, which results in effective reel.
        
        GPIO.output(m1, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))  			#GPIO.output() set one of the GPIO pin to High in a sequencial order, which results in defined rotation of stepper motor (i.e.clockwise or anti-clockwise)
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
        b+=1
           
# dereel is used to move the glassrods downwards      
def dereel():
    print("Dereel")
    d=0 
    while d<950: 
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
       
def relayon():                 	                                             # relayon() is used to turn on the light
     print("lights on")
     GPIO.output(rp,GPIO.HIGH)
def relayoff(): 				                                             # relayoff() is used to turn off light
    print("lights off")
    GPIO.output(rp,GPIO.LOW)

blynk.on("connected") 			                                              # Used to connect to the blynk
def blynk_connected():
    print ("ccc")
   
@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected') 
    blynk.connect()			                                                   # Reconnect to Blynk when it is disconnected 


@blynk.on("V1")
def V1_write_handler(value): 		                                            #reads the value(state) of virtual pin V1
    print(value[0])
    val1= int(float(value[0])) 	                                                # val1 stores the value[0] i.e,LSB(Least significant bit) of value
    if val1 == 1:				                                                # when val1==1 then the reel function executes.
        reel()
    elif val1 == 0:			                                                    # when val1==0 then the dereel function  executes.
        dereel()
 
@blynk.on("V2")
def V2_write_handler(value):
    print(value[0])
    val2= int(float(value[0]))
    if val2 == 1:
        relayon()                                                             # when Val2==1 then the relayon function executes
    elif val2 == 0:			
        relayoff()                                                            # when Val2==0 then the relayoff function executes 			
       

while True:
    blynk.run() 

