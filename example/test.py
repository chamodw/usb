import usb.core, usb.util
import time

dev = usb.core.find(idVendor=0x9999, idProduct=0xffff)
dev.set_configuration(1)

ld = -1
lt = time.time()

psize = 4096
ls = 0

s=''.join([chr(x) for x in range(64)])

while True:
	##v = int(raw_input())
	##dev.ctrl_transfer(usb.util.CTRL_OUT | usb.util.CTRL_TYPE_VENDOR, 0x23, v, 0, '')
	d = dev.read(0x81, 64, 0, 100)
	print d
	ls += len(d)
	dev.write(0x02, s, 0, 100)
	if ls > 1024*1024:
		t = time.time()
		#print ls, t - lt, round(ls/(t - lt))
		lt = t
		ls = 0
