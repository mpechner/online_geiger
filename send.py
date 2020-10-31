import aprs
import argparse

parser = argparse.ArgumentParser(description="Will send telemetry for a might ohm geiger counter.")
parser.add_argument('--call', required=True,help='callsign dash sid')
parser.add_argument('--passcode', required=True,help='aprsis password')
args = parser.parse_args()

# to generate the passcode: https://apps.magicbug.co.uk/passcode/

call = args.call
password = args.passcode

frames = [ 
"{call}>APDW16:!3721.34N/12159.52WImightyohm Geiger, Santa Clara, CA",
"{call}>APDW16::{call} :PARM.fake",
"{call}>APDW16::{call} :UNIT.foos/bar",
"{call}>APDW16::{call} :EQNS.0,0.5,0",
"{call}>APDW16::{call} :BITS.11111111,Learning Telemetery",
]

conn = aprs.TCP(call.encode('utf-8'), password.encode('utf-8'))
conn.start() 
for frame in frames:
    #print(frame.format(call=call).encode('utf-8'))
    conn.send(frame.format(call=call).encode('utf-8'))

ii=5
val = 33
conn.send("{call}>APDW16:T#{seq:03d},{val:03d}".format(call=call, seq=ii, val=val).encode('utf-8'))
