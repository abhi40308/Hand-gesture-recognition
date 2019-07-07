import RPi.GPIO as GPIO
from time import sleep
L1=14
L2=23
L3=25
L4=8
L5=10
L6=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L2,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L3,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L4,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L5,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L6,GPIO.OUT)

while(1):
file = open('input.txt','r')
xx = file.readlines()
value = xx[len(xx)-1]
try:
value = int(value)
if(value == 1):
print('1')
GPIO.output(L1,True)
sleep(0.02)
GPIO.output(L1,False)
elif(value==2):
print('2')
GPIO.output(L2,True)
sleep(0.03)
GPIO.output(L2,False)
elif(value ==3):
print('3')
GPIO.output(L3,True)
sleep(0.03)
GPIO.output(L3,False)
elif(value==4):
	print('4')
GPIO.output(L4,True)
sleep(0.03)
GPIO.output(L4,False)
elif(value ==5):
print('5')
GPIO.output(L5,True)
sleep(0.03)
GPIO.output(L5,False)
elif(value==6):
print('6')
GPIO.output(L6,True)
sleep(0.03)
GPIO.output(L6,False)

except:
pass
GPIO.cleanup()