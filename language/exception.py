import time

def testException():
	try:
		x = 5/0

	except Exception as e: # Exception
		print ("error: <%s>" % (e))
		#raise # make program exit
		return 0

	else: # Success
		print ("Success <%d>", x)
		return 1

	finally: # Always run
		print ("Finally")

# 1 - Success, 0 - sFail
print ("return %d" % (testException()))

while 1:
	time.sleep(10)