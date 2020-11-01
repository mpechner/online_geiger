# APRS Geiger Counter
I'm not the first one, won't be the last. 

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

##Python APRS library
Ran these 2 commands and I was in business:
* sudo apt-get install pip3
* sudo apt-get install aprs

The issue with this library is even though a version 7 makes it look mature, the code might be abandoned.
Found a couple of obvious errors in the initial readme.

The calls for the TCP class takes bytes, not strings. So b"foo" or FOVAR.encode('utf-8') is your friend.

## Current State as of now ad future plans
Since I do not have the board soldered yet, there is not imput. Send.py just sends a fixed set of packets.
Will eventually be a cron job reading the board and sending the packets.

Coming **Thanksgiving 2020**

# References
__Dire Wolf user guide__ https://github.com/wb2osz/direwolf/blob/master/doc/User-Guide.pdf
__Dire Wolf Repo__ git clone git@github.com:wb2osz/direwolf.git
__APRS Passcode Generator__ https://apps.magicbug.co.uk/passcode/
__Dire Wolf Telemetery__https://github.com/wb2osz/direwolf/blob/master/doc/APRS-Telemetry-Toolkit.pdf
__APRS Website__ http://www.aprs.org/
__APRS Reference__ http://www.aprs.org/doc/APRS101.PDF
__APRS BASH__ https://s55ma.radioamater.si/2017/07/27/send-aprs-objects-or-telemetry-via-bash/