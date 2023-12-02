import time
import requests
import json


print ("\nThousandEyes find Dashboard ID")
time.sleep(1)   #pause 1 second

aid=input("Account Group ID: ")
bearer=input("Bearer Token: ")
full_bearer=("Bearer"+bearer)

#retrive dashboard data call the api

get_dashboardID= ("https://api.thousandeyes.com/v7/dashboards?aid="+aid)  #api url

#declare headers

headers1={
    'Authorization': full_bearer,
    'Content-Type': 'application/hal+json;charset=UTF-8',
}

#make the api call to get the dashboard data and save into a folder

resp = requests.get(get_dashboardID,headers=headers1)

#save the response as json

pretty_json=json.loads(resp.text)

show=(json.dumps(pretty_json, indent=2))

resp_json=resp.json()

with open ('dashboard_ID_list.txt','w+') as u:
    print(show,file=u)
    print(show)


