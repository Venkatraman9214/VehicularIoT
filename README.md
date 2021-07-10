Beta testing of the VeNet Model

https://user-images.githubusercontent.com/18708096/125177942-0c308e80-e1ae-11eb-89c0-5ccc04da4bd3.mp4



https://user-images.githubusercontent.com/18708096/125177945-10f54280-e1ae-11eb-98d9-1ae5b4f7ea0d.mp4

# VehicularIoT
This project works on two main protocols one is ad-hoc network over a P2P protocol and two, its the MQTT message querying that is built on top of this. 

I have added the basic set up configurations for everyone to replicate such a system and use it as per their desires.

The pin configurations are mentioned in the beginning for better understanding. For other hardware builds, here is a quick run-down.

--The Chassis Base. This is an acrylic plastic base, precut with several holes to mount components. You can get it on variable sizes on amazon or adafruit website based on your needs.
![Scaled Vehicle](https://user-images.githubusercontent.com/18708096/125177903-ab08bb00-e1ad-11eb-803f-d9a8a43f1b21.jpeg)

--Motor Mounts. Some of the kits use acrylic for this as well, others use aluminum brackets. Mounting the motors is probably the thing that confuses most users so I’ll illustrate that in detail.

--DC Motors. These 6-volt motor have a surprising amount of torque for their size.

--Wheels. A car isn’t much use without wheels! These chassis kits use four plastic wheels, with tire treads that work well on both smooth surfaces and carpet. All on Amazon or Adafruit website.

--Encoder Wheels. There are four plastic disks which are meant to mount to the motor shafts, on the opposite sides from the wheels. They have a series of slots in them as they are designed to be used with an optical source-sensor to provide feedback on motor speed and wheel position. The PWM pulses received from the motor driver pretty much gets translated to usable metrics because of these slows. I have attached the csv files where you will see the RPS values.

--Battery Holder- We use a 12V rechargeable battery. RPi has both 5v and 3v pins, so you wouldn't need anything excessive to power up the RPi.

--Mounting Hardware. All of the nuts, bolts and spacers you will need to put the chassis together.  You’ll need to supply more hardware to mount your own components on the base.
Misc Parts – Some of the hot glued thick edges were from an expensive mfg purchased at the university.

Stay tuned for more updates!
