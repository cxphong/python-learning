import subprocess

# Not overwrite
p = subprocess.Popen("wget http://dl.fiot.vn/app-debug.apk -P /Users/caoxuanphong/Downloads/",
                 stdout=subprocess.PIPE,
                 shell=True)
(output, err) = p.communicate()

#Overwite
p = subprocess.Popen("wget -N http://dl.fiot.vn/app-debug.apk -P /Users/caoxuanphong/Downloads/",
                 stdout=subprocess.PIPE,
                 shell=True)
(output, err) = p.communicate()