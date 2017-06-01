# importing the requests library
import requests
 
# api-endpoint
URL = "https://trendcloud.net/alpha/index.php/apis/ControllerApisCheckVersion"
 
# defining a params dict for the parameters to be sent to the API
PARAMS = {'device_version': 20}
 
# sending get request and saving the response as response object
r = requests.post(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()
 
print ("data %s" % data)

print ("%s %s %s" % (data['has_new_ver'], data['version'], data['bin_url']))
