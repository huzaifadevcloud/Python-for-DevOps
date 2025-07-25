import requests
import os
import json
import dotenv
import subprocess


# Load .env variables
dotenv.load_dotenv()

url = os.getenv("JENKINS_URL")
username = os.getenv("JENKINS_USER")
password = os.getenv("JENKINS_TOKEN")

print("🔍 Script started")

#Starting a service using subprocess
service_name = str(input("Enter the service you want to start : "))
result = subprocess.run(["systemctl", "start", service_name], capture_output=True, text=True) # Run the command to start the service

# Check if the service started successfullyS
if result.returncode == 0:
    print(f"{service_name} started successfully")
else:
    print(f"Failed to start {service_name}")
    print(result.stderr)

response = requests.get(f"{url}api/json", auth=(username, password), verify=False)
if response.status_code == 200:
    try :
        data = response.json()
    except json.JSONDecodeError:
        print("Failed to decode JSON. Response was likely HTML.")
        exit(1)
    # Extract the list of jobs from the JSON response   
    # The 'jobs' key contains a list of job dictionaries
    jobs = data.get("jobs", [])
    print("Jenkins Jobs:")

    for job in jobs:
        job_name = job['name']
        job_url = f"{url}job/{job_name}/"
        print(job_name) # Print the name of each job
        
        #Use the 'auth' parameter to send requests with HTTP Basic Auth:
        #Accessing the Job page to get the latest Build ran.
        response_job = requests.post(f"{job_url}api/json", auth = (username, password),verify=False) #Verify=False is used to ignore SSL certificate warnings

        try:
            buildnumberJson = json.loads(response_job.text) #json.loads() function is used to parse a JSON string and convert it into a Python data structure (usually a dictionary or a list).
    
        except:
            print ("Failed to parse json")
            exit(1)

        if buildnumberJson.get("lastBuild") is None:
            print(f"No builds found for job: {job_name}")
            continue  #continue statement is used inside loops (for or while) to skip the current iteration and move to the next one immediately.

        totalbuilds = buildnumberJson["lastBuild"] #   totalbuilds = buildnumberJson["lastBuild"] # Extract the 'lastBuild' dictionary
        runs = totalbuilds["number"] # Extract the 'number' key from the 'lastBuild' dictionary
    
    
        totalsuccess = totalfailure = totalmissing = 0
        
        #Iterate over the job build runs to get the build status for each
        for build in range(1,runs):
            buildurl= f"{job_url}{build}/api/json"
            print(buildurl)
            buildstatus = [] # Initialize an empty list to store build status  
            try:
                response = requests.post(buildurl, auth = (username, password),verify=False) 
                buildstatus = json.loads(response.text)    # Parse the JSON response
            except Exception as e:
                totalmissing =  totalmissing + 1  
            if "result" in buildstatus:
                if buildstatus["result"] == "SUCCESS" :
                    totalsuccess = totalsuccess + 1
                if buildstatus["result"] == "FAILURE" :
                    totalfailure = totalfailure + 1
                
else:
    print(f"Failed to fetch jobs. Status Code: {response.status_code}")
    print("Response:", response.text)



#Generate Output numbers

print(f"total builds:{runs}")
print(f"total succeeded builds:{totalsuccess}")
print(f"total failed builds:{totalfailure}")
print(f"total skipped builds:{totalmissing}")
