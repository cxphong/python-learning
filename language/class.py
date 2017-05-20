import picamera

class Test(object):

	def test_camera(cls):		
		print ("%d" % (cls.test_camera_hardware()))

	def test_camera_hardware(cls):
		print ("test_camera_hardware")

		try:
			camera = picamera.PiCamera()
		except Exception as e:
			print e
			print "Camera hardware is broken or it didn't connect"
			return 1
		else:
			print "Camera hardware is ok"
			return 0


test = Test()
test.test_camera()

Test().test_camera()