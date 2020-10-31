

Tried to use Direwolf.  But I did not find an obvious manor to start the service in igate node then exit.  Tried using kissutil.  kissutil only sent to channels, not to igate.

Found the aprs python library.  It just works.


sudo apt-get install pip3
sudo apt-get install aprs

https://github.com/wb2osz/direwolf

steps taken from 
https://github.com/wb2osz/direwolf/blob/master/doc/User-Guide.pdf
Do read it.  The document has many more details.  This is just the most basic cookie currer, assume all works list of commands.


sudo apt-get install cmake libasound2-dev libudev-dev
sudo apt-get install build-essential

git clone git@github.com:wb2osz/direwolf.git
cd direwolf

Decide if running dev, master, or latest stable version.

mpechner@mpechner-virtual-machine:~/direwolf$ git branch -a
* master
  remotes/origin/1.6
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/gh-pages
  remotes/origin/master

git checkout dev
mkdir build
cd build
cmake -DUNITTEST=1..
make -j4
make test
sudo make install
make install-conf

edit ~/direwolf.conf

find "MYCALL" and set to your callsign
MYCALL W6XRL4

https://apps.magicbug.co.uk/passcode/


https://github.com/wb2osz/direwolf/blob/master/doc/APRS-Telemetry-Toolkit.pdf

direwolf -c ~/Desktop/packet.sh

need to get it to send once and quit.  Or send to igate once up


OK, moving from direwolf to APRS python package

Using dirwilf was able to figure out the packets to send.

