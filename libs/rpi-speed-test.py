import subprocess
import time
import os
import sys

interface = sys.argv[1] 

rx0 = -1
tx0 = -1

print ("Listening %s" % interface);

while (1):
	rx = os.popen("cat /sys/class/net/" + interface + "/statistics/rx_bytes").read().rstrip()
	tx = os.popen("cat /sys/class/net/" + interface + "/statistics/tx_bytes").read().rstrip()	

	if (rx0 != -1):
		rxs = (int(rx) - rx0)/1024
		txs = (int(tx) - tx0)/1024

		print ("Received %.2f KB/s, Sent %.2f KB/s" % (rxs, txs))

	rx0 = int(rx)
	tx0 = int(tx)

	time.sleep(1)