#!/usr/bin/env python3
import os

seq = 0
if os.path.exists('/var/run/geiger'):
	fi = open('/var/run/geiger', 'r') 
	seq = int(fi.read())
	fi.close()

seq += 1
fi = open('/var/run/geiger', 'w')
int(fi.write(str(seq)))
fi.close()
val = 110


str = "T#{seq:03d},{val}".format(seq=seq, val=val)
print(str, end='')
