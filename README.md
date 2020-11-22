# APRS Geiger Counter
I'm not the first one, won't be the last. 

So now 2 working aproaches.

## Dire Wolf - First Pass
I made a pass using Dire Wolf. Problem is since this is in my house I did not feel 
the need to pass the packets over the air. Just run an igate and send the data. 

Dire Wolf seems to have a lot of overhead. Configure a CBEACON with an infocmd option that 
called a python script to read the board. Granted, the raspberry pi has nothing else to do.
Truthfuly, working on this initially at 3AM, this did not GROK until the next day. Thought 
it could not be done. When tired, go to bed. I might have done this. Still might to publish another approach.

I found his bash script that uses ncat to send the packets:
https://s55ma.radioamater.si/2017/07/27/send-aprs-objects-or-telemetry-via-bash/

Seems workable, but I tend to not use bash as a programming language. I use it as a wrapper to setup environments for 
python.

So other than getting the packes generated while I was playing, Dire Wolf got me no where.
## Dire Wolf Pass 2
Took about an hour.  You will see geiger_reading.py is called from a CBEACON.  For notw it will create /var/run/geiger to hold the latest seq number.  Need a better place for the file so direwolf does not have to be run as root.

Once I get the geiger counter assembled I will add the code to read the data.

##Python APRS library
Ran these 2 commands and I was in business:
* sudo apt-get install python3-pip
* sudo pip3 install aprs

The issue with this library is even though a version 7 makes it look mature, the code might be abandoned.
Found a couple of obvious errors in the initial readme.

The calls for the TCP class takes bytes, not strings. So b"foo" or FOVAR.encode('utf-8') is your friend.

## MightyOhm Wiring to Raspberrypi
http://mightyohm.com/forum/viewtopic.php?t=4524
Pin marked 'blk' on the ftdi pins is pin1
MO   Pi
1....6
4....8
5...10

https://mightyohm.com/blog/products/geiger-counter/usage-instructions/
CSV lines;  CPS, #####, CPM, #####, uSv/hr, ###.##, SLOW|FAST|INST
I am posting "uSv/hr"

## Current State as of now and future plans
Since I do not have the board soldered yet, there is not imput. Send.py just sends a fixed set of packets.
Will eventually be a cron job reading the board and sending the packets.

Coming **Thanksgiving 2020**


# References
* Dire Wolf user guide https://github.com/wb2osz/direwolf/blob/master/doc/User-Guide.pdf
* Dire Wolf Repo git clone git@github.com:wb2osz/direwolf.git
* APRS Passcode Generator https://apps.magicbug.co.uk/passcode/
* Dire Wolf Telemetery https://github.com/wb2osz/direwolf/blob/master/doc/APRS-Telemetry-Toolkit.pdf
* APRS Website http://www.aprs.org/
* APRS Reference http://www.aprs.org/doc/APRS101.PDF
* APRS BASH https://s55ma.radioamater.si/2017/07/27/send-aprs-objects-or-telemetry-via-bash/
