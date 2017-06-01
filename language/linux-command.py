import subprocess

p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print ("Today is %s %s" % (output, err))

p = subprocess.Popen(["ls", "-l"],stdout=subprocess.PIPE)
(output, err) = p.communicate()
print ("Today is %s %s" % (output, err))