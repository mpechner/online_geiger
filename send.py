import os
import argparse
import serial
import aprs

seq = 0
seqfile = "/home/pi/seqfile"
def next_seq():
	global seq, seqfile

	if os.path.exists(seqfile):
		fi = open(seqfile, 'r') 
		seq = int(fi.read())
		fi.close()
	
	if seq > 10000:
		seq=0
	seq += 1
	fi = open(seqfile, 'w')
	int(fi.write(str(seq)))
	fi.close()
	return seq



def read_value():
    ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    x=ser.readline()
    return float(x.split(b',')[5])

parser = argparse.ArgumentParser(description="Will send telemetry for a might ohm geiger counter.")
parser.add_argument('--call', required=True,help='callsign dash sid')
parser.add_argument('--passcode', required=True,help='aprsis password')
args = parser.parse_args()

# to generate the passcode: https://apps.magicbug.co.uk/passcode/

call = args.call
password = args.passcode

frames = [ 
"{call}>APDW16:!3721.34N/12159.52WImightyohm Geiger, Santa Clara, CA",
"{call}>APDW16::{call} :PARM.Geiger",
"{call}>APDW16::{call} :UNIT.uSv/hr,",
"{call}>APDW16::{call} :EQNS.0,1.0,0",
"{call}>APDW16::{call} :BITS.11111111,background radiation",
]

conn = aprs.TCP(call.encode('utf-8'), password.encode('utf-8'))
conn.start() 
for frame in frames:
    #print(frame.format(call=call).encode('utf-8'))
    conn.send(frame.format(call=call).encode('utf-8'))

next_seq()
conn.send("{call}>APDW16:T#{seq:03d},{val:04.2f}".format(call=call, seq=seq, val=read_value()).encode('utf-8'))


