Using Message Query

1. Go to mosquitto-debian repo 
https://mosquitto.org/blog/2013/01/mosquitto-debian-repository/
2. Follow all the instructions, update your RPi and get the latest MQTT version.
3. Install the mosquitto-clients
sudo apt-get install mosquitto-clients.
4. There are multiple ways in which MQTT can be tested, the most basic one is via command-line. We will see that below.
	4.1. Broker Intialization- (a) Open Terminal, go to /etc/mosquitto/mosquitto.conf.
				   (b) Edit, the config file, add -> listener 1883:<IP of the broker>
				   (c) Check the permissions on the log files, db files etc.
				   (d) Run mosquitto with new config as follow:
					mosquitto -c /etc/mosquitto/mosquitto.conf

	4.2. Client Initialization- (a) For local connection (subscription window)- This also where the broker is running. You can do something similar to make the broker run elsewhere.
					mosquitto_sub -t <topic> -d {for daemon}
				    (b) For remote connection- Open remote terminal, and type the following
					mosquitto_pub -h <Broker IP> -t <topic> -m  <message>
				    (c) You may also publish from within the subscriber (just to check connections)
5. For deploying a script, you will have to download a Python MQTT client called Paho-client via
	pip3 install paho-mqtt.
	5.1. Broker Initialization- This is exactly the same as before.

	5.2  Client Intialization- (a) Import the paho-client into your script. The main socket connections that you need to watch out for is ->client.connect("<broker IP>", port). Remember the double quotes for python 3.
				   (b) Keep the broker listening on the port. By default the port is 1883, however you can check the listening ports.
				   (c) For publishing utilities, ``import paho.mqtt.publish as publish''
				   