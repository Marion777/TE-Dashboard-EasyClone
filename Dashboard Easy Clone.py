import time
import requests
import json


print ("\nThousandEyes Dashboard Easy Clone")
time.sleep(1)   #pause 1 second

token=input("\nInput the Bearer Token. Example:(30cea081-58f0-4c81-a1ef-ab2b60bca3c8)\nBearer ")

full_token1=("Bearer "+token)

#input the dashboard id

dashboard_id=input("Input the dashboard ID \nDashboardID: ")

#retrive dashboard data call the api

get_dashboard= ("https://api.thousandeyes.com/v7/dashboards/"+dashboard_id) #api url

#declare headers

headers1={
    'Authorization': full_token1,
    'Content-Type': 'application/hal+json;charset=UTF-8',
}

#make the api call to get the dashboard data and save into a folder

resp = requests.get(get_dashboard,headers=headers1)

#save the response as json

pretty_json=json.loads(resp.text)

show=(json.dumps(pretty_json, indent=2))

#resp_json=resp.json()

with open ('result.txt','w+') as u:
    print(show,file=u)

time.sleep(1)

#input the new bearer token of the new Organization

token_2=input("\nAdd the token of the org where you want to clone the Dashboard!\n"
              "If it is the same org repeat the token\nBearer ")
full_token_2=("Bearer "+token_2)

new_aid=input("\nAdd the account group ID you would like to clone the dashboard.(If many split them by comma ','):")
new_aid_loop=new_aid.split(",")
new_name=input ("\nName the new dashboard:")

#make changes on the file and replace on the new_result.txt

with open ('result.txt') as f:
    data = json.load(f)
    for title in data['title']:
        data['title'] = new_name

with open('edited_result.json','w+') as u:
    print(json.dumps(data),file=u)

time.sleep(2)

#push the cloned dashboard to the new account

push_dashboard="https://api.thousandeyes.com/v7/dashboards"

#declare headers

headers1={
    'Authorization': full_token_2,
    'Content-Type': 'application/hal+json;charset=UTF-8',
}

#open the new folder and make the Post request

for i in new_aid_loop:
    with open('edited_result.json', 'rb') as payload:
        params={'aid':i} #replace query
        resp2=requests.post(push_dashboard,params=params,data=payload,headers=headers1)

pretty_json1=json.loads(resp2.text)
show1=(json.dumps(pretty_json1, indent=2))
print(show1)

with open('cloned_dashboard_detail.txt','w') as e:
    print(show1,file=e)

