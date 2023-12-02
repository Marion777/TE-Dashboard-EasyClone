import time
import requests
import json

print ("Find my Account Group ID")

token=input("\nPlease input the Bearer Token! Example:(30cea081-58f0-4c81-a1ef-ab2b60bca3c8)\nBearer ")

full_token1=("Bearer "+token)

#retrive dashboard data call the api

get_accountID= ("https://api.thousandeyes.com/v7/account-groups")  #api url

#declare headers

headers1={
    'Authorization': full_token1,
    'Content-Type': 'application/hal+json;charset=UTF-8',
    'Transfer_Encoding': 'chunked'
}

#make the api call to get the dashboard data and save into a folder

r = requests.get(get_accountID,headers=headers1)

pretty_json=json.loads(r.text)

show=(json.dumps(pretty_json, indent=2))
print(show)

with open ('AccountGroup_ID.txt','w+') as u:
    print(show,file=u)




