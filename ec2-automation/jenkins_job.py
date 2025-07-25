import requests
import os
import json
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

url = os.getenv("JENKINS_URL")
username = os.getenv("JENKINS_USER")
password = os.getenv("JENKINS_TOKEN")

print("🔍 Script started")

#Use the 'auth' parameter to send requests with HTTP Basic Auth:
#Accessing the Job page to get the latest Build ran.
response = requests.post(f"{url}api/json", auth = (username, password),verify=False)


try:
    buildnumberJson = json.loads(response.text)
    
except:
    print ("Failed to parse json")
    exit(1)

if "lastBuild" in buildnumberJson:  
    totalbuilds = buildnumberJson["lastBuild"]
    runs = totalbuilds["number"]
    
else:
    print ("Failed to get build")

#Iterate over the job build runs to get the build status for each

totalsuccess = totalfailure = totalmissing = 0

for build in range(1,runs):
    buildurl= f"{url}{build}/api/json"
    print(buildurl)
    buildstatus = []
    try:
        response = requests.post(buildurl, auth = (username, password),verify=False)
        buildstatus = json.loads(response.text)
    except Exception as e:
        totalmissing =  totalmissing + 1  
    if "result" in buildstatus:
        if buildstatus["result"] == "SUCCESS" :
            totalsuccess = totalsuccess + 1
        if buildstatus["result"] == "FAILURE" :
            totalfailure = totalfailure + 1


#Generate Output numbers

print(f"total builds:{runs}")
print(f"total succeeded builds:{totalsuccess}")
print(f"total failed builds:{totalfailure}")
print(f"total skipped builds:{totalmissing}")
