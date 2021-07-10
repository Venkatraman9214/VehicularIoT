
import math
import time
import board
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
import RPi.GPIO as GPIO
from time import sleep
#from timer import Timer
import threading
import sys
import queue
from queue import Queue
#from threading import _thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



in1 = 27
in2 = 17
ena = 22
# For Motor 2 (FR),
in3 = 24
in4 = 23
enb = 25

#Associate the pins of Motor Driver 2 to the GPIO ports on Pi:
# For Motor 3 (RL),
in7 = 20
in8 = 16
end = 21
# For Motor 4 (RR),
in5 = 19
in6 = 13
enc = 26



# Pi GPIO setups and vehicle initial operation setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(end,GPIO.OUT)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(enc,GPIO.OUT)


GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)

GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)



p1=GPIO.PWM(ena,1000)
p2=GPIO.PWM(enb,1000)
p3=GPIO.PWM(enc,1000)
p4=GPIO.PWM(end,1000)

p1.start(40)
p2.start(40)
p3.start(40)
p4.start(40)

#print("\n")
#print("The default speed & direction of motor is LOW & Forward.....")
#print("r-run  x-stop w-forward s-backward 1-low speed 2-high speed a-left d-right t-exit")
#print("\n")    

q=queue.Queue()

start_timer=time.time()
gpio=1
gpio2=5
gpio3=14
gpio4=6
rpm1= 0
rpm2=0
rpm3=0
rpm4=0
interval=0
interval2=0
interval3=0
interval4=0
dc1=40
dc2=40
dc3=40
dc4=40
count1=0
count2=0
count3=0
count4=0
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

def init_interrupt1():
#	global count,d,interval,rpm,dist_km,dist_meas,km_per_sec,km_per_hour
	GPIO.add_event_detect(1, GPIO.FALLING, callback = calculate_elapse1 , bouncetime = 20)

def init_interrupt2():
	GPIO.add_event_detect(5, GPIO.FALLING, callback = calculate_elapse2, bouncetime = 20)
def init_interrupt3():
	GPIO.add_event_detect(14, GPIO.FALLING, callback = calculate_elapse3, bouncetime = 20)
def init_interrupt4():
	GPIO.add_event_detect(6, GPIO.FALLING, callback = calculate_elapse4, bouncetime = 20)

#intervalnow=time.time()-start_timer
def calculate_elapse1(channel):				# callback function
	global count1,count2,count3,count4,d, start_timer,start_timer2,start_timer3,start_timer4,interval,interval2,interval3,interval4
	count1+=1
	interval += time.time()-start_timer		# elapse for every 1 complete rotation made!
	start_timer = time.time()

def calculate_elapse2(channel):				# callback function
	global count1,count2,count3,count4,d, start_timer,start_timer2,start_timer3,start_timer4,interval,interval2,interval3,interval4

	count2+=1
	interval += time.time()-start_timer		# elapse for every 1 complete rotation made!
	start_timer = time.time()

def calculate_elapse3(channel):				# callback function
	global count1,count2,count3,count4,d, start_timer,start_timer2,start_timer3,start_timer4,interval,interval2,interval3,interval4

	count3+=1
	interval += time.time()-start_timer		# elapse for every 1 complete rotation made!
	start_timer = time.time()

def calculate_elapse4(channel):				# callback function
	global count1,count2,count3,count4,d, start_timer,start_timer2,start_timer3,start_timer4,interval,interval2,interval3,interval4

	count4+=1
	interval += time.time()-start_timer		# elapse for every 1 complete rotation made!
	start_timer = time.time()


def calculate_speed1():
	global count1,count2,count3,count4,start_timer,interval,interval2,interval3,interval4,rpm1,rpm2,rpm3,rpm4

	if interval !=0:
		rpmA = count1/(interval)
		rpm1= (rpmA*3.14*2)/20
def calculate_speed2():
	global count1,count2,count3,count4,start_timer,interval,interval2,interval3,interval4,rpm1,rpm2,rpm3,rpm4


	if interval !=0:
		rpmA = count2/(interval)
		rpm2= (rpmA*3.14*2)/20
def calculate_speed3():
	global count1,count2,count3,count4,start_timer,interval,interval2,interval3,interval4,rpm1,rpm2,rpm3,rpm4

	if interval !=0:
		rpmA = count3/(interval)
		rpm3= (rpmA*3.14*2)/20
def calculate_speed4():
	global count1,count2,count3,count4,start_timer,interval,interval2,interval3,interval4,rpm1,rpm2,rpm3,rpm4

	if interval !=0:
		rpmA = count4/(interval)
		rpm4= (rpmA*3.14*2)/20

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = LSM6DS33(i2c)


def movement():

	global dc1,dc2,dc3,dc4,rpm1,rpm2,rpm3,rpm4,count1,count2,count3,count4,interval,interval2,interval3,interval4, start_timer1
	init_interrupt1()
	
	init_interrupt2()
	init_interrupt3()
	init_interrupt4()

	d=1
	for i in range (0,20):
		j=0
			
		while(j<1000):
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
			GPIO.output(in5,GPIO.HIGH)
			GPIO.output(in6,GPIO.LOW)
			GPIO.output(in7,GPIO.HIGH)
			GPIO.output(in8,GPIO.LOW)

	#		calculate_speed1()
			for dc1 in range(40,85,5):
				p1.ChangeDutyCycle(dc1)
			for dc2 in range(40,85,5):
				p2.ChangeDutyCycle(dc2)
			for dc3 in range(40,85,5):
				p3.ChangeDutyCycle(dc3)
			for dc4 in range(40,85,5):
				p4.ChangeDutyCycle(dc4)
		
	#			p1.ChangeDutyCycle(80)
	#			p2.ChangeDutyCycle(80)
	#			p3.ChangeDutyCycle(80)
	#			p4.ChangeDutyCycle(80)
		#	for dc2 in range(80,15,-5):
		#		p1.ChangeDutyCycle(dc2)
		#	for dc3 in range(80,15,-5):
		#		p4.ChangeDutyCycle(dc3)
		#	calculate_speed1()
		#	calculate_speed2()
		#	calculate_speed3()
		#	calculate_speed4()
	#		print("Thread1",calculate_speed1())		
	#		print(dc1,",",dc2,",",dc3,",",dc4,",",interval1,",",count1,",",gpio,",",calculate_speed1(),",",interval2,",",count2,",",gpio2,",",rpm2,",","interval3",",",count3,",",gpio3,",",rpm3,",","interval2",",",count4,",",gpio4,",",rpm4,",%.2f,%.2f,%.2f"%(sensor.acceleration),",%.2f,%.2f,%.2f"%(sensor.gyro))


			j=j+1
		i=i+1
	for i in range (0,50):
		j=0
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
		GPIO.output(in5,GPIO.HIGH)
		GPIO.output(in6,GPIO.LOW)
		GPIO.output(in7,GPIO.HIGH)
		GPIO.output(in8,GPIO.LOW)
		while(j<10000):

			
			p1.ChangeDutyCycle(20)
			p2.ChangeDutyCycle(80)
			p3.ChangeDutyCycle(80)
			p4.ChangeDutyCycle(20)
			#for dc2 in range(40,15,-5):
			dc1=20
			#p1.ChangeDutyCycle(dc2)
			#for dc3 in range(40,15,-5):
			dc4=20
			#p4.ChangeDutyCycle(dc3)
			j=j+1
		i=i+1
#
	#print("stop")
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
	GPIO.output(in5,GPIO.LOW)
	GPIO.output(in6,GPIO.LOW)
	GPIO.output(in7,GPIO.LOW)
	GPIO.output(in8,GPIO.LOW)







def sensors():
#	global x, count,interval, start_timer
#
#	i2c = board.I2C()  # uses board.SCL and board.SDA
#	sensor = LSM6DS33(i2c)
#	init_interrupt1()
#	init_interrupt2()
#	init_interrupt3()
#	init_interrupt4()
	i=0

	while True:
##		global start_timer,x
		calculate_speed1()
		calculate_speed2()
		calculate_speed3()
		calculate_speed4()
		print(dc1,",",dc2,",",dc3,",",dc4,",",interval,",",count1,",",gpio,",",rpm1,",",count2,",",gpio2,",",rpm2,",",count3,",",gpio3,",",rpm3,",",",",count4,",",gpio4,",",rpm4,",%.2f,%.2f,%.2f"%(sensor.acceleration),",%.2f,%.2f,%.2f"%(sensor.gyro))

#		print(dc1,",",dc2,",",dc3,",",dc4,",",interval,",",count1,",",gpio,",",rpm1,",",count2,",",gpio2,",",rpm2,",",count3,",",gpio3,",",rpm3,",",count4,",",gpio4,",",rpm4,",%.2f,%.2f,%.2f"%(sensor.acceleration),",%.2f,%.2f,%.2f"%(sensor.gyro))
		#i=i+1
		sleep(0.5)


#movement()
threading.Thread(target=movement).start()
threading.Thread(target=sensors).start()		
#q.join()

